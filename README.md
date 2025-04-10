# Fantasy-Weapon-Name-Generator

# ⚔️ Fantasy Weapon Name Generator

A fine-tuned language model that generates fantasy weapon names and descriptions, designed as part of a Machine Learning Internship assignment for Red Panda Games.

---

## 🚀 Project Overview

This project fine-tunes the `distilgpt2` model on a filtered subset of the Dungeons & Dragons character backstories dataset. The model is trained to generate creative weapon names and lore-rich descriptions.

---

## 🧠 Model Task

- **Dataset Source**: [D&D Character Backstories Dataset](https://huggingface.co/datasets/MohamedRashad/dnd_characters_backstories)
- **Filtered Content**: Sentences that mention fantasy weapons (sword, axe, staff, etc.)
- **Model**: `distilgpt2` (lightweight GPT-2 variant)
- **Training**: 4 epochs, batch size = 2

---

## 🛠 How to Run

### 🔹 Clone and Install Dependencies

```bash
git clone https://github.com/AgarwalBhavya/fantasy-weapon-generator.git
cd fantasy-weapon-generator
pip install -r requirements.txt
