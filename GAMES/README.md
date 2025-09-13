# Hra života (Game of Life) – Pygame

Tento projekt je implementací slavné **Conwayovy Hry života** v Pythonu pomocí knihovny **Pygame**.  
Aplikace umožňuje ručně měnit buňky, spouštět/stopovat simulaci a vkládat předdefinované vzory (block, blinker, glider).

---

## 🚀 Spuštění

### 1. Nainstaluj závislosti
Projekt potřebuje Python 3 a knihovnu `pygame`:

```bash
pip install pygame
```

### 2. Spusť aplikaci
```bash
python game_of_life.py
```

---

## 🎮 Ovládání

- **Levým klikem**: přepne stav buňky (živá/mrtvá).
- **Pravým klikem**: vloží vybraný vzor (např. glider).
- **Tlačítka dole**:
  - `block`, `blinker`, `glider` – výběr vzoru pro vkládání.
  - `start` – spustí simulaci.
  - `stop` – zastaví simulaci.
  - `clear` – vymaže celé plátno.
- **Klávesové zkratky**:
  - `SPACE` – spustí / zastaví simulaci.
  - `C` – vymaže plátno.

---

## ⚙️ Konfigurace

V horní části kódu lze změnit:
- `CELL_SIZE` – velikost jedné buňky (px).
- `GRID_WIDTH`, `GRID_HEIGHT` – rozměry mřížky.
- `FPS` – rychlost simulace (generace za sekundu).

---

## 📦 Struktura kódu

- **`Button`** – třída pro vykreslování a ovládání tlačítek.
- **`Grid`** – správa buněk, pravidla hry, vykreslování.
- **`PatternManager`** – uchovává předdefinované vzory.
- **`GameOfLife`** – hlavní logika hry (pygame loop, UI, události).

---

## 📸 Ukázka

*(sem můžeš vložit screenshot aplikace)*

---

## 📚 O hře

Hra života je **celulární automat**, který vytvořil matematik John Conway v roce 1970.  
Každá buňka na mřížce má dva možné stavy: živá nebo mrtvá. Každá generace se vyhodnocuje podle jednoduchých pravidel:
- Živá buňka s 2–3 sousedy přežívá.
- Mrtvá buňka se 3 sousedy ožívá.
- Jinak buňka zaniká nebo zůstává mrtvá.

---
