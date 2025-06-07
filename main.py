from lox.scanner import Scanner

if __name__ == "__main__":
    fonte = 'var nome = "Diene"; print(nome); // comentário'
    scanner = Scanner(fonte)
    tokens = scanner.scan_tokens()
    for token in tokens:
        print(token)
