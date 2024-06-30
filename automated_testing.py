# Discord username: painter_99; Discord name: painter99

# Importujeme knihovny, které potřebujeme pro psaní testů
import pytest
from playwright.sync_api import sync_playwright

# Test 1: Otevření stránky a kontrola titulu
def test_open_page_and_check_title(page):
    # Načteme stránku pomocí URL
    page.goto("https://fedoraproject.org/atomic-desktops/silverblue/download")
    # Ověříme, že titulek stránky je "Get Fedora"
    assert page.title() == "Get Fedora"

# Test 2: Kontrola existence tlačítka pro stažení
def test_check_download_button(page):
    # Načteme stránku pomocí URL
    page.goto("https://fedoraproject.org/atomic-desktops/silverblue/download")
    # Vyhledáme tlačítko pro stažení podle částečné URL v atributu href
    download_button = page.query_selector("a[href*='silverblue/download']")
    # Ověříme, že tlačítko existuje (není None)
    assert download_button is not None, "Download button not found"

# Test 3: Kontrola odkazu na dokumentaci
def test_check_documentation_link(page):
    # Načteme stránku pomocí URL
    page.goto("https://fedoraproject.org/atomic-desktops/silverblue/download")
    # Vyhledáme odkaz na dokumentaci podle přesné URL v atributu href
    doc_link = page.query_selector("a[href='https://docs.fedoraproject.org/en-US/fedora-silverblue/']")
    # Ověříme, že odkaz existuje (není None)
    assert doc_link is not None, "Documentation link not found"
