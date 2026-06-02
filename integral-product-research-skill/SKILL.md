---
name: integral-product-research-skill
description: Integral product research, value proposition, hypothesis validation, and PRD workflow for AI agents and product teams. Use when Codex or another AI agent needs to conduct market research, discover segments, map Advanced Jobs To Be Done (AJTBD), prioritize segments with ABCDX, identify riskiest assumptions with RAT, plan Customer Development experiments, craft value propositions, or write detailed product requirements for designers and developers.
---

# integral-product-research-skill

## 1. Краткое описание

Используй этот skill, чтобы провести продуктовую команду через полный цикл от идеи до требований:

1. Интерпретировать продуктовую идею, рынок, пользователей и ограничения.
2. Найти потенциальные сегменты и альтернативы.
3. Сформулировать Advanced Jobs To Be Done для каждого сегмента.
4. Оценить привлекательность сегментов через ABCDX и числовой скоринг.
5. Оценить TAM / SAM / SOM с явными допущениями и уровнем уверенности.
6. Сформулировать гипотезы ценности, связанные с job, болью, барьером и desired outcome.
7. Определить самые рискованные предположения через RAT.
8. Спланировать минимальные проверки гипотез.
9. Превратить приоритетные или подтвержденные гипотезы в PRD, пригодный для UX/UI-дизайна, разработки, QA и аналитики.

Skill поддерживает три режима:

- `market-research` — исследование рынка, сегментов, jobs, альтернатив, конкурентов и фокуса.
- `craft-value-proposition` — гипотезы ценности, RAT, эксперименты и messaging.
- `product-requirements` — детальный Product Requirements Document для реализации.

## 2. Когда использовать skill

Используй skill, когда нужно:

- исследовать рынок для новой или существующей продуктовой идеи;
- найти сегменты, у которых может быть сильная боль и готовность платить;
- перейти от демографического описания аудитории к jobs, контекстам и desired outcomes;
- оценить привлекательность сегментов не только по размеру рынка, но и по боли, доступности, willingness-to-pay, competition и product fit;
- сформулировать ценностные гипотезы и офферы, связанные с реальными jobs;
- определить, какие предположения могут “убить” продукт, если окажутся неверными;
- спланировать problem interviews, smoke tests, concierge MVP, Wizard of Oz, pricing tests и другие минимальные проверки;
- написать PRD, по которому живые команды и AI-агенты смогут проектировать и разрабатывать продукт без потери смысла исследования.

## 3. Когда не использовать skill

Не используй skill как основной инструмент, если задача состоит только в:

- написании рекламного слогана без исследования;
- генерации UI-макета без продуктового контекста;
- технической отладке кода;
- финансовом моделировании без продуктовых гипотез;
- юридической экспертизе или медицинском заключении;
- доказательстве размера рынка без внешних источников.

Если пользователь просит точные рыночные данные, актуальные конкурентные сведения, цены, законы или статистику, используй внешние источники и явно цитируй их. Не подменяй проверку генерацией модели.

## 4. Входные данные skill

Базовый вход:

```yaml
product_idea: ""
industry: ""
target_geography: ""
business_model: ""
current_stage: ""
known_audience: ""
known_problem: ""
known_solution: ""
competitors: []
available_data: []
constraints:
  budget: ""
  time: ""
  team: ""
  technology: ""
  legal: ""
desired_output_depth: "brief | standard | deep | exhaustive"
language: "ru"
```

Если часть данных отсутствует, продолжай работу. Не останавливайся, кроме случаев, когда невозможно определить саму продуктовую идею или целевой контекст. Все пробелы помечай как `Unknown / требует проверки`.

## 5. Основные команды

### `market-research`

Используй для исследования рынка, поиска сегментов, jobs, альтернатив, конкурентов, оценки TAM / SAM / SOM и рекомендации фокуса.

Подробная инструкция: `commands/market-research.md`.
Шаблоны: `templates/market-research-report.md`, `templates/segment-scorecard.md`, `templates/jtbd-job-map.md`.

### `craft-value-proposition`

Используй после первичного выбора сегментов и jobs, чтобы сформулировать гипотезы ценности, разложить value mechanisms, найти барьеры и драйверы, применить RAT и составить план проверок.

Подробная инструкция: `commands/craft-value-proposition.md`.
Шаблоны: `templates/value-proposition-plan.md`, `templates/rat-experiment-card.md`.

### `product-requirements`

Используй, чтобы превратить приоритетные или подтвержденные гипотезы ценности в детальные требования для дизайна, разработки, QA, аналитики и релиза.

Подробная инструкция: `commands/product-requirements.md`.
Шаблон: `templates/product-requirements-document.md`.

## 6. Методология

### AJTBD / Advanced Jobs To Be Done

Трактуй AJTBD как расширенный Jobs To Be Done: единица анализа — работа, которую человек или организация пытается выполнить в конкретной ситуации, а не персона или демография.

Анализируй:

- main job;
- related jobs;
- functional jobs;
- emotional jobs;
- social jobs;
- context;
- trigger;
- struggling moments;
- current alternatives;
- barriers;
- drivers;
- hiring criteria;
- firing criteria for alternatives;
- desired outcomes;
- job graph;
- mechanics, через которые продукт помогает выполнить job лучше, быстрее, дешевле, безопаснее или с меньшей когнитивной нагрузкой.

Формат job:

```text
Когда [ситуация], я хочу [выполнить работу], чтобы [получить прогресс / outcome].
```

Не подменяй job фичей. `Получить автоматический отчет` может быть фичей; job обычно звучит как `понять, где теряются клиенты, чтобы принять решение о следующем улучшении`.

### ABCDX-сегментация

Классифицируй сегменты:

- `A` — высокий потенциал, высокая боль, высокая готовность платить, сильный product fit.
- `B` — хороший потенциал, но есть ограничения по каналу, бюджету, зрелости или частоте боли.
- `C` — умеренная ценность; можно обслуживать стандартизированно, но не фокусироваться.
- `D` — низкий приоритет: слабая боль, слабый бюджет, слабый fit или высокая стоимость привлечения.
- `X` — неизвестный, непроверенный или противоречивый сегмент, требующий исследования.

Оценивай каждый сегмент по боли, частоте, срочности, бюджету, willingness-to-pay, доступности каналов, конкуренции, альтернативам, сложности продажи, сложности внедрения, стратегической ценности, product fit, объему рынка, качеству данных и неопределенности.

### RAT / Riskiest Assumption Test

RAT нужен, чтобы найти предположения, которые могут убить продукт, если окажутся неверными.

Классифицируй риски:

- `problem risk` — проблема не существует или недостаточно болезненна;
- `segment risk` — выбранный сегмент не тот;
- `value risk` — предложенная ценность не важна;
- `willingness-to-pay risk` — пользователи не готовы платить;
- `channel risk` — невозможно эффективно достучаться до сегмента;
- `solution risk` — решение не помогает выполнить job;
- `usability risk` — пользователи не смогут пользоваться решением;
- `operational risk` — решение невозможно устойчиво доставлять;
- `legal/compliance risk` — есть ограничения закона, отрасли или политики;
- `technical risk` — реализация слишком сложна, дорогая или нестабильна.

Для каждой рискованной гипотезы указывай формулировку, тип риска, почему критично, способ проверки, минимальный эксперимент, критерий успеха, критерий провала, данные, срок, стоимость и решение после проверки: `continue`, `change`, `defer`, `kill`.

### Интегральный пайплайн

1. Исследуй рынок, контекст и альтернативы.
2. Найди 5–12 возможных сегментов.
3. Построй jobs map и job graph для приоритетных сегментов.
4. Оцени сегменты через ABCDX и числовой скоринг.
5. Сформулируй гипотезы ценности.
6. Выяви самые рискованные предположения через RAT.
7. Спланируй минимальные эксперименты.
8. Переведи приоритетные или подтвержденные гипотезы в требования.
9. Закрой связь между `segment → job → pain → desired outcome → value hypothesis → requirement → metric`.

## 7. Общие правила агента

Всегда:

- отделяй факты от гипотез;
- явно помечай предположения;
- не выдумывай статистику, источники, интервью и результаты экспериментов;
- указывай уровень уверенности;
- указывай, какие данные нужно проверить;
- работай итерационно;
- задавай уточняющие вопросы только если без них невозможно продолжить;
- если данных мало, делай лучший возможный черновой анализ и помечай зоны неопределенности;
- не подменяй jobs фичами;
- не подменяй сегменты демографией;
- не пиши абстрактные УТП без связи с job, болью, барьером и desired outcome;
- не пиши продуктовые требования без user story, acceptance criteria, edge cases и ограничений;
- не рекомендуй фокус только на основании размера рынка — учитывай боль, доступность, willingness-to-pay и риск проверки.

Обязательное правило доказательности:

> Агент не должен считать результат исследования доказанным, если он основан только на генерации модели. Любой вывод о рынке, сегменте, боли, willingness-to-pay или размере рынка должен быть помечен как гипотеза до подтверждения внешними данными, интервью, аналитикой или экспериментами.

## 8. Правила работы с неопределенностью

Используй метки:

- `Fact` — подтверждено предоставленными данными, источником, аналитикой, интервью или экспериментом.
- `Hypothesis` — логичный вывод модели или команды, но нет проверки.
- `Assumption` — допущение для расчета или планирования.
- `Unknown` — данных недостаточно.
- `Needs validation` — критичный вывод, требующий проверки.

Если данных мало:

1. Сформируй черновую карту рынка и сегментов.
2. Не используй категоричные формулировки.
3. Укажи, какие данные нужны для повышения confidence.
4. Предложи самые дешевые проверки.
5. Не превращай гипотезы в требования без маркировки риска.

## 9. Правила отделения фактов от гипотез

В отчетах добавляй блок `Evidence & Assumptions` или помечай строки таблиц:

| Claim | Type | Evidence | Confidence | Validation Needed |
|---|---|---|---|---|
| Сегмент имеет частую боль | Hypothesis | Логика рынка, неподтверждено | Low | 8–12 problem interviews |

Запрещено писать: `рынок составляет $X`, если нет источника или явных допущений. Пиши: `Гипотетическая диапазонная оценка TAM: X–Y при допущениях A, B, C; confidence: Low`.

## 10. Правила оценки уверенности

Используй шкалу:

- `High` — подтверждено несколькими надежными источниками, пользовательскими данными или экспериментами; противоречий мало.
- `Medium` — есть частичные данные, похожие кейсы или 1–2 источника; остаются важные пробелы.
- `Low` — основано в основном на генерации модели, экспертной логике или непроверенных допущениях.
- `Unknown` — нет данных для оценки.

Confidence не равен привлекательности сегмента. Сегмент может иметь высокий потенциальный score и низкую уверенность; в таком случае присваивай ABCDX `X` или `B/X` до проверки.

## 11. Правила приоритизации

Используй скоринг 0–100:

```text
Segment Score =
Pain Intensity * 0.20 +
Frequency * 0.15 +
Willingness To Pay * 0.15 +
Accessibility * 0.15 +
Market Size * 0.10 +
Product Fit * 0.15 +
Low Competition Advantage * 0.05 +
Strategic Value * 0.05
```

Каждый фактор оценивай по шкале 0–100. Если фактор неизвестен, не ставь произвольный высокий балл: используй 40–50 как нейтральное допущение или `Unknown`, а затем явно укажи, как проверить.

ABCDX назначай после скоринга, но корректируй класс с учетом confidence:

- `A`: score обычно 75–100 и confidence не ниже Medium.
- `B`: score 60–74 или высокий score с ограничением.
- `C`: score 45–59, умеренная ценность.
- `D`: score ниже 45 или сильные барьеры.
- `X`: данных недостаточно, противоречивые признаки или критичный риск не проверен.

## 12. Правила генерации требований

PRD должен сохранять цепочку смысла:

```text
Segment → Context → Job → Pain → Desired Outcome → Value Hypothesis → Feature / Flow → Requirement → Acceptance Criteria → Metric
```

Для каждого важного требования указывай:

- purpose;
- user problem;
- linked job;
- linked value hypothesis;
- behavior;
- inputs / outputs;
- states;
- validation rules;
- permissions;
- errors;
- empty / loading states;
- edge cases;
- analytics events;
- acceptance criteria в формате Given / When / Then;
- dependencies;
- risks and assumptions.

Не включай в MVP фичи, которые не проверяют ключевую job или главную гипотезу ценности.

## 13. Форматы вывода

Выбирай формат по команде:

- `market-research`: используй `templates/market-research-report.md`.
- `craft-value-proposition`: используй `templates/value-proposition-plan.md`.
- `product-requirements`: используй `templates/product-requirements-document.md`.

Если пользователь просит `brief`, сокращай детали, но сохраняй: факты/гипотезы, confidence, risks, next validation. Если `exhaustive`, расширяй таблицы, добавляй scoring rationale, experiment cards и requirement checklist.

## 14. Критерии качества результата

Результат считается качественным, если:

- можно действовать без дополнительных объяснений;
- сегменты описаны через контекст, jobs, боль, доступность и WTP, а не только демографию;
- jobs сформулированы в формате ситуации, работы и progress outcome;
- segment scoring прозрачен и воспроизводим;
- TAM / SAM / SOM имеют источники или явные допущения;
- value proposition связана с job, pain, barrier, desired outcome и alternative;
- RAT выделяет 3–7 самых опасных предположений;
- эксперименты минимальны, измеримы и имеют decision rules;
- PRD пригоден для дизайна, разработки, QA и аналитики;
- все непроверенные выводы помечены как гипотезы.

## 15. Ограничения

- Skill не заменяет внешнее исследование рынка, интервью, аналитику, юридическую экспертизу или технический discovery.
- Skill не должен создавать видимость доказанности без evidence.
- Для актуальных рыночных данных, конкурентов, regulation, цен и статистики используй внешнюю проверку.
- Для regulated industries добавляй legal/compliance risk и советуй экспертную проверку.

## 16. Примеры использования

```text
Use integral-product-research-skill market-research for:
product_idea: AI assistant for independent therapists to summarize sessions and prepare follow-ups
industry: mental health SaaS
geography: US
business_model: subscription
current_stage: idea
```

```text
Use integral-product-research-skill craft-value-proposition based on the top 2 segments from the market research. Generate 8 value hypotheses per segment and a RAT plan for the 5 riskiest assumptions.
```

```text
Use integral-product-research-skill product-requirements to write a PRD for an MVP that validates the main job and value hypothesis. Include user stories, acceptance criteria, edge cases, analytics, release plan, and risks.
```
