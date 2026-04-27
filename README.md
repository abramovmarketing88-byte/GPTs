# Модульная AI-система генерации лендингов

## Что делает система

Этот проект превращает набор отдельных prompt-файлов в производственный, расширяемый пайплайн:

1. Анализ аудитории (`audience_analysis.txt`)
2. Сегментация (`segmentation.txt`)
3. Выявление болей/барьеров (`pain_points.txt`)
4. Синтез инсайтов (`insights_synthesis.txt`)
5. Проектирование структуры лендинга (`landing_structure.txt`)
6. Генерация копирайтинга (`copywriting.txt`)
7. Финальный QA-ревью (`review_qa.txt`)

Архитектура разделена на:

- `skills/` — изолированные функции-шаги (один prompt = один skill);
- `orchestrator/` — центральный контроллер выполнения шагов;
- `utils/llm.py` — абстракция вызова LLM;
- `runner.py` — CLI-точка входа для локального запуска.

## Структура проекта

```text
project_root/
├── prompts/
│   ├── audience_analysis.txt
│   ├── segmentation.txt
│   ├── pain_points.txt
│   ├── insights_synthesis.txt
│   ├── landing_structure.txt
│   ├── copywriting.txt
│   └── review_qa.txt
├── skills/
│   ├── audience.py
│   ├── segmentation.py
│   ├── pains.py
│   ├── insights.py
│   ├── structure.py
│   ├── copywriting.py
│   ├── review.py
│   ├── common.py
│   └── registry.py
├── orchestrator/
│   └── pipeline.py
├── utils/
│   └── llm.py
├── config.py
├── runner.py
└── README.md
```

## Установка

1. Нужен Python 3.10+.
2. Рекомендуется виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Дополнительные зависимости не требуются (по умолчанию используется `mock` LLM wrapper).

## Запуск

Базовый запуск:

```bash
python runner.py "Avito marketing service"
```

Запуск с выводом промежуточных шагов:

```bash
python runner.py "Avito marketing service" --show-steps
```

Показать карту prompt-файлов и их ролей:

```bash
python runner.py --list-prompts
```

## Как добавить новый prompt (новый шаг)

1. Добавьте новый `.txt` в `prompts/` (текст prompt — на английском).
2. Создайте новый skill-модуль в `skills/`:
   - загрузка prompt через `load_prompt(...)`;
   - вызов `call_llm(...)`;
   - возврат результата.
3. Добавьте шаг в `SKILL_HANDLERS` в `orchestrator/pipeline.py` в нужной позиции.
4. Добавьте описание роли в `PIPELINE_SPECS` в `skills/registry.py`.

## Как изменить pipeline

Файл: `orchestrator/pipeline.py`

Можно менять:

- порядок шагов;
- контекст, передаваемый между шагами;
- состав выходных данных;
- финальный шаг и формат результата.

## LLM wrapper

`utils/llm.py` содержит функцию:

```python
def call_llm(prompt: str, input_data: str) -> str:
```

Сейчас это mock-реализация. Для подключения реальной модели:

1. Обновите `config.py`;
2. Добавьте провайдер в `call_llm`;
3. Добавьте обработку ошибок, ретраи и логирование.

## Языковые требования

- Все prompt-файлы: **English**
- Код: **English**
- Документация: **Russian**
