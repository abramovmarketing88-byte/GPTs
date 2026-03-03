# MODULE_REGISTRY

Назначение: единая карта маршрутизации модулей для ROOT.

Каноническое правило уточнений:
"Если критически не хватает данных, задай ровно 1 уточняющий вопрос, который снимает главный риск ошибки. Если можно выполнить задачу без вопроса — не задавай его."

Каноническая anti-hallucination формула:
"Не выдумывать факты, метрики, кейсы, цитаты и источники. Если данных нет — явно сказать 'нет данных' и перечислить, что нужно предоставить."

Правило совместимости форматов:
Внутренние артефакты модулей публикуются только внутри FINAL_PROMPT / FINAL_PIPELINE / FINAL_SPEC. Внешний формат всегда: SELECTED_MODULES, ASSUMPTIONS, FINAL_PROMPT/FINAL_PIPELINE/FINAL_SPEC, QUICK_CHECKLIST.

| module_id | filename | when_to_use | inputs_needed | output_type | forbidden | quality_bar |
|---|---|---|---|---|---|---|
| PROMPT_CRAFT | PROMPT_CRAFT.md | Улучшить или создать промт | Цель, формат, ограничения | SINGLE_PROMPT_TEMPLATE, MULTI_PROMPT_PIPELINE_TEMPLATE | Абстрактный промт без цели | Промт исполним, формат однозначен |
| CONTEXT_ENGINEERING | CONTEXT_ENGINEERING.md | Собрать и структурировать контекст | Цели, источники, ограничения, scope | PROJECT_CONTEXT | Шум, нерелевантный контекст | Контекст достаточен и компактен |
| INTENT_ENGINEERING | INTENT_ENGINEERING.md | Прояснить цели, приоритеты, trade-offs | Business outcome, user outcome, метрики, риски | PRIORITY_STACK, TRADE_OFF_RULES | Невнятный intent | Приоритеты формализованы |
| SPEC_ENGINEERING | SPECIFICATION_ENGINEERING.md | Сформировать автономную спецификацию | Scope, требования, критерии, риски | AUTONOMOUS_SPEC | Непроверяемые критерии | Спецификация автономна и тестируема |
| COPYWRITING | COPYWRITING_ENGINE.md | Создать продающий текст | ЦА, оффер, канал, CTA | Copy draft/variants | Обещания без подтверждений | Ясный оффер и CTA |
| CRO_AUDIT | CRO_AUDIT_ENGINE.md | Найти барьеры конверсии | Данные по воронке, экран, сегменты | CRO findings + hypotheses | Гарантии роста без оснований | Гипотезы связаны с барьерами |
| TECH_DEBUG | TECH_DEBUG_ENGINE.md | Диагностика технических проблем | Логи, шаги воспроизведения, окружение | Debug plan + hypothesis tree | Root cause без проверок | Проверяемый план и критерии фикса |
| RESEARCH_SUMMARY | RESEARCH_ENGINE.md | Сжать и структурировать исследования | Материалы, цель анализа, формат | Insight summary | Искажение источников | Выводы трассируются к данным |

Явная связка SPEC:
- TASK_TYPE = SPEC_ENGINEERING
- filename = SPECIFICATION_ENGINEERING.md
