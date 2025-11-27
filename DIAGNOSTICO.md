# 🔍 Diagnóstico - Problema de Conexão

## Erro: ERR_CONNECTION_REFUSED

Se você está vendo a mensagem do Flask dizendo que está rodando, mas o navegador não consegue conectar, siga estes passos:

### ✅ Passo 1: Verifique se o servidor está realmente rodando

No terminal onde o Flask está rodando, você deve ver:
```
 * Running on http://127.0.0.1:5000
```

**Se NÃO aparecer essa linha**, o servidor não iniciou corretamente.

### ✅ Passo 2: Verifique se há erros no terminal

Procure por mensagens de erro em vermelho no terminal. Erros comuns:
- `TemplateNotFound` - Template não encontrado
- `ModuleNotFoundError` - Módulo não encontrado
- `ImportError` - Erro ao importar

### ✅ Passo 3: Teste manualmente

1. **Pare o servidor** (CTRL+C no terminal)
2. **Execute novamente**:
   ```bash
   cd servico_diario
   python app.py
   ```
3. **Observe as mensagens** - há algum erro?

### ✅ Passo 4: Verifique se a porta está livre

Execute no PowerShell:
```powershell
netstat -ano | findstr :5000
```

Se aparecer algo com `LISTENING`, a porta está em uso.

### ✅ Passo 5: Tente outra porta

Se a porta 5000 estiver ocupada, edite `servico_diario/app.py` e mude:
```python
app.run(host='127.0.0.1', port=5001, debug=True, use_reloader=False)
```

E acesse: http://127.0.0.1:5001/

### ✅ Passo 6: Verifique o firewall

O Windows Firewall pode estar bloqueando. Tente:
1. Desativar temporariamente o firewall
2. Ou adicionar exceção para Python

### ✅ Passo 7: Teste com curl ou PowerShell

No PowerShell, execute:
```powershell
Invoke-WebRequest -Uri http://127.0.0.1:5000/ -UseBasicParsing
```

Se funcionar, o problema é no navegador. Se não funcionar, o problema é no servidor.

---

## 🚨 Solução Rápida

Se nada funcionar, tente:

1. **Feche TODOS os terminais**
2. **Abra um NOVO terminal**
3. **Execute**:
   ```bash
   cd C:\Projetos\Quoter\servico_diario
   python app.py
   ```
4. **Aguarde** até ver "Running on http://127.0.0.1:5000"
5. **Acesse** http://127.0.0.1:5000/ no navegador

---

## 📝 Informações para Debug

Se o problema persistir, me informe:

1. **Mensagem completa** que aparece no terminal quando você executa `python app.py`
2. **Resultado** do comando `netstat -ano | findstr :5000`
3. **Versão do Python**: `python --version`
4. **Versão do Flask**: `pip show flask`

