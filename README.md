# 🧠 Automação Web com IA e Browser-use

Este projeto demonstra como utilizar inteligência artificial para automatizar ações em um navegador real usando a biblioteca [browser-use](https://github.com/browser-use/browser-use). O objetivo foi simular uma jornada de compra completa no site [saucedemo.com](https://www.saucedemo.com/) e gerar um teste automatizado em Cypress com base nas ações realizadas.

> ⚠️ Este repositório faz parte de um estudo pessoal. Nenhuma informação sensível real foi utilizada.

---

## 🚀 O que a automação faz:

1. Acessa o site `https://www.saucedemo.com`
2. Realiza login com o usuário `standard_user` e senha `secret_sauce`
3. Adiciona dois produtos ao carrinho:
   - Sauce Labs Backpack
   - Sauce Labs Fleece Jacket
4. Finaliza a compra usando dados fictícios
5. Valida a mensagem final "Thank You For Your Order!"
6. Gera um teste em Cypress com esses passos

---

## 🧩 Tecnologias usadas:

- [Python 3.11+](https://www.python.org/)
- [browser-use](https://github.com/browser-use/browser-use)
- [Playwright](https://playwright.dev/)
- [OpenAI API](https://platform.openai.com/)
- Cypress (teste gerado via IA)

---

## 🛠 Como executar:

1. Instale o Python>=3.11

2. Instale a biblioteca browser-use:
```bash
pip install browser-use
```

3. Para funcionalidades de memória (recomendado para Python < 3.13)
```bash
pip install "browser-use[memory]"
```

4. Instale o navegador Chromium para o Playwright:
```bash
playwright install chromium --with-deps --no-shell
```

5. Para usar a interface CLI interativa:
```bash
pip install browser-use[cli]
browser-use
```

6. Configure o .env
```bash
OPENAI_API_KEY=sua-chave-aqui
```

7. Execute o script principal
```bash
python3 main.py
```

O navegador será aberto e a automação será realizada. Ao final, um código Cypress será gerado e exibido no terminal.

## ▶️ Demonstração: 
![automacaoIA](https://github.com/user-attachments/assets/dddac014-e488-4d59-826b-73e11a8670eb)


## 📚 Referência e créditos:
Este projeto usa a biblioteca [browser-use](https://github.com/browser-use/browser-use), criada por: Müller e Žunič (2024)

```bibtex
@software{browser_use2024,
  author = {Müller, Magnus e Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
``` 
