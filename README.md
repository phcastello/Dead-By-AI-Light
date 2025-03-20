# 🎮 Dead By AI light

## 📝 About the Project
**Dead By AI light** is a 2D game inspired by Dead by Daylight, designed to be played by both humans and trained artificial intelligences. The game focuses on the interaction between a killer and four survivors, where AI can be trained to improve its gameplay strategies over time.

## 📌 Main Features
- **Game Modes**: Choose to play as a **Killer** or **Survivor**, or enter **AI training mode**.
- **Trainable AI**: The artificial intelligence can learn survival and chase techniques throughout matches.
- **Procedural Map Generation**: Each match takes place on a randomly generated map.
- **Neural Network Visualization**: A panel displays the AI's activated neurons in real-time, including the last layer representing the chosen actions.
- **Skill Checks**: Quick-time events for survivors when repairing generators and attempting to escape the killer.
- **Movement and Combat**:
  - The Killer is slightly faster than survivors.
  - Survivors need to be hit twice before they can be captured.
  - Survivors can struggle to escape from hooks and while being carried.

## 🏗 Project Structure

```
📂 DeadByAILight/
│── 📂 assets/         # Images, sounds, animations
│── 📂 data/           # Saves, configurations
│── 📂 ai/             # AI code
│   ├── neural_network.py
│── 📂 game/           # Core game code
│   ├── game.py
│   ├── characters.py  # Survivor and Killer
│   ├── objects.py     # Generator and Hook
│   ├── map.py         # Map generation
│── 📂 ui/             # Graphical interface
│   ├── menu.py
│   ├── neural_visualizer.py
│── main.py            # Entry point
```

## 🖥 Technologies Used
- **Python** (main language)
- **Pygame** (game rendering)
- **NumPy** (mathematical operations for AI)
- **Matplotlib** (AI progress visualization)
- **PyTorch** (AI training)

## 🚀 How to Run the Game
1. Clone the repository:
   ```sh
   git clone https://github.com/phcastello/DeadByAILight.git
   cd DeadByAILight
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the game:
   ```sh
   python main.py
   ```

## 🤖 How to Train the AI
1. Access the training menu in the game.
2. Choose the training parameters.
3. Track the AI's learning process through the visualization interface.

## 🏗 Future Roadmap
- [ ] Improve AI behavior for Killer and Survivors.
- [ ] Create different maps and obstacles.
- [ ] Implement sound and visual effects.
- [ ] Balance gameplay for both humans and AI.

## 📜 License
This project is open-source and distributed under the MIT license.

## 📢 Contribution
If you want to contribute, fork the repository, create a new branch, and submit a pull request!

