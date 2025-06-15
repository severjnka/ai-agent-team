from crewai import Crew, Agent, Task
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

analyst = Agent(name="Analyst", role="ТЗ-аналитик", goal="Составить спецификацию требований", backstory="Анализирует задачи и цели пользователя", llm=llm)
developer = Agent(name="Developer", role="Разработчик", goal="Реализовать код", backstory="Создает эффективный код по архитектуре", llm=llm)
tester = Agent(name="Tester", role="Тестировщик", goal="Разработать и выполнить тесты", backstory="Обеспечивает стабильность", llm=llm)

crew = Crew(
    agents=[analyst, developer, tester],
    tasks=[
        Task("Собери требования", agent=analyst),
        Task("Напиши код", agent=developer),
        Task("Протестируй код", agent=tester)
    ]
)

crew.kickoff()
