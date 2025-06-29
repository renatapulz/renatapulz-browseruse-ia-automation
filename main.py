import tempfile
import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent, BrowserSession
from langchain_openai import ChatOpenAI

async def main():
    # Cria uma pasta temporária única para user_data_dir (força a limpeza de sessão)
    with tempfile.TemporaryDirectory() as tmpdir:
        browser_session = BrowserSession(
            incognito=True,
            user_data_dir=tmpdir,
            headless=False
        )

        agent = Agent(
            task="""
Acesse o site https://www.saucedemo.com/, faça login com o usuário `standard_user` e a senha `secret_sauce`. Em seguida, adicione os produtos "Sauce Labs Backpack" e "Sauce Labs Fleece Jacket" ao carrinho. Clique no carrinho, e inicie o checkout. Na próxima tela adicione um nome, sobrenome e código postal quaisquer e clique em continuar. Confirme que os dois produtos estão listados e finalize a compra. Valide que a compra foi concluída com sucesso exibindo a mensagem "Thank You For Your Order!". Por fim, retorne o código dessa automação usando Cypress.
""",
            llm=ChatOpenAI(model="gpt-4o"),
            browser_session=browser_session,
        )
        await agent.run()

asyncio.run(main())