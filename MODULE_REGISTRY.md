# MODULE_REGISTRY

Назначение: единый реестр модулей для ROOT-оркестратора.

Каноническое правило уточнений:
"Если критически не хватает данных, задай ровно 1 уточняющий вопрос, который снимает главный риск ошибки. Если можно выполнить задачу без вопроса — не задавай его."

Каноническая anti-hallucination формула:
"Не выдумывать факты, метрики, кейсы, цитаты и источники. Если данных нет — явно сказать 'нет данных' и перечислить, что нужно предоставить."

Правило совместимости форматов:
Внутренние артефакты модулей публикуются только внутри FINAL_PROMPT / FINAL_PIPELINE / FINAL_SPEC. Внешний формат всегда: SELECTED_MODULES, ASSUMPTIONS, FINAL_PROMPT/FINAL_PIPELINE/FINAL_SPEC, QUICK_CHECKLIST.

| module_id | filename | purpose | when_to_use | dependencies | output_type |
|---|---|---|---|---|---|
| PROMPT_CRAFT | PROMPT_CRAFT.md | Создание рабочих промтов и prompt-pipeline | Нужен новый промт или улучшение существующего | CONTEXT_ENGINEERING, INTENT_ENGINEERING | SINGLE_PROMPT_TEMPLATE, MULTI_PROMPT_PIPELINE_TEMPLATE |
| CONTEXT_ENGINEERING | CONTEXT_ENGINEERING.md | Сбор и нормализация проектного контекста | Нужно структурировать вводные, ограничения, источники | STRUCTURING_ENGINE | PROJECT_CONTEXT |
| INTENT_ENGINEERING | INTENT_ENGINEERING.md | Формализация целей, приоритетов, trade-offs | Цели расплывчаты или конфликтуют | CONTEXT_ENGINEERING | PRIORITY_STACK, TRADE_OFF_RULES |
| SPEC_ENGINEERING | SPECIFICATION_ENGINEERING.md | Автономная спецификация под исполнение | Нужно ТЗ/спецификация/acceptance criteria | INTENT_ENGINEERING, CONTEXT_ENGINEERING | AUTONOMOUS_SPEC |
| COPYWRITING | COPYWRITING_ENGINE.md | Создание маркетинговых и продуктовых текстов | Нужны тексты для лендинга/email/ads | PROMPT_CRAFT, INTENT_ENGINEERING | Copy Draft, A/B Variants |
| CRO_AUDIT | CRO_AUDIT_ENGINE.md | Аудит конверсии и гипотезы роста | Нужен CRO-аудит или улучшение воронки | RESEARCH_SUMMARY, COPYWRITING | CRO Findings, Hypothesis Backlog |
| TECH_DEBUG | TECH_DEBUG_ENGINE.md | Диагностика техпроблем и план фикса | Ошибки, падения, деградации, 500 | SPEC_ENGINEERING | Hypothesis Tree, Verification Plan |
| RESEARCH_SUMMARY | RESEARCH_ENGINE.md | Синтез исследований и интервью | Нужно сжать и обобщить материалы | SUMMARIZATION, STRUCTURING | Insight Summary, Evidence Table |
| SUMMARIZATION | SUMMARIZATION_ENGINE.md | Краткое резюме длинных материалов | Нужен короткий конспект/summary | RESEARCH_SUMMARY | Executive Summary, Key Points |
| STRUCTURING | STRUCTURING_ENGINE.md | Преобразование хаотичных данных в структуру | Нужен скелет документа/ответа/плана | CONTEXT_ENGINEERING | Section Outline, Structured Skeleton |
| QA_VALIDATION | QA_VALIDATION.md | Контроль качества финального результата | Нужна финальная проверка перед выдачей | OUTPUT_NORMALIZER | QA Verdict, Defect List |
| ROUTING_DIAGNOSTICS | ROUTING_DIAGNOSTICS.md | Проверка корректности маршрутизации | Есть сомнения в выборе TASK_TYPE/модулей | ROOT_GPT_ORCHESTRATOR | Routing Report, Conflict Flags |
| OUTPUT_NORMALIZER | OUTPUT_NORMALIZER.md | Нормализация внутренних артефактов в ROOT формат | Нужно собрать единый внешний ответ | Все активированные модули | ROOT Output Protocol Response |

Явная связка SPEC:
- TASK_TYPE = SPEC_ENGINEERING
- filename = SPECIFICATION_ENGINEERING.md
