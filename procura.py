import os
from PyPDF2 import PdfReader

def search_word_in_pdfs(directory, search_terms):
    """
    Procura por palavras específicas em todos os arquivos PDF em um diretório.
    
    Args
        directory (str): Caminho do diretório contendo os arquivos PDF.
        search_terms (list): Lista de palavras ou frases a serem procuradas.
        
    Returns:
        dict: Um dicionário com os arquivos PDF e as páginas onde as palavras foram encontradas.
    """
    results = {}
    
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(directory, file)
            try:
                reader = PdfReader(pdf_path)
                results[file] = []
                
                for page_number, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if any(term.lower() in text.lower() for term in search_terms):
                        results[file].append(page_number + 1)
            
            except Exception as e:
                print(f"Erro ao processar {file}: {e}")
    
    return {file: pages for file, pages in results.items() if pages}

# Entrada do usuário
if __name__ == "__main__":
    directory = 'procura/notas'
    search_terms = input("Digite as palavras ou frases a serem procuradas, separadas por vírgulas: ").strip().split(',')
    search_terms = [term.strip() for term in search_terms]
    
    if os.path.isdir(directory):
        search_results = search_word_in_pdfs(directory, search_terms)
        
        if search_results:
            print("\nPalavras encontradas:")
            for file, pages in search_results.items():
                print(f"\nArquivo: {file}")
                print(f"Páginas: {', '.join(map(str, pages))}")
        else:
            print("\nNenhuma palavra encontrada nos arquivos PDF.")
    else:
        print("Diretório inválido.")
