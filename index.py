from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
)
from PyQt5.QtCore import Qt, QTimer


class TreeClicker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.growth_points = 0  
        self.gardener_count = 0  
        self.gardener_cost = 20  
        self.growth_per_gardener = 2 

        self.setWindowTitle("Выращивай дерево!")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        
        self.growth_label = QLabel(f"Очки роста: {self.growth_points}", self)
        self.growth_label.setAlignment(Qt.AlignCenter)
        self.growth_label.setStyleSheet("font-size: 20px;")
        self.layout.addWidget(self.growth_label)

        
        self.grow_button = QPushButton("Вырастить дерево", self)
        self.grow_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.grow_button.clicked.connect(self.grow_tree)
        self.layout.addWidget(self.grow_button)

        
        self.gardener_label = QLabel(
            f"Садовники: {self.gardener_count} (помогают расти на {self.gardener_count * self.growth_per_gardener} очков/сек)",
            self
        )
        self.gardener_label.setAlignment(Qt.AlignCenter)
        self.gardener_label.setStyleSheet("font-size: 16px;")
        self.layout.addWidget(self.gardener_label)

        
        self.hire_button = QPushButton(f"Нанять садовника - {self.gardener_cost} очков роста", self)
        self.hire_button.setStyleSheet("font-size: 16px; padding: 8px;")
        self.hire_button.clicked.connect(self.hire_gardener)
        self.layout.addWidget(self.hire_button)

        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.auto_grow)
        self.timer.start(1000)  

    def grow_tree(self):
        """Рост дерева при нажатии кнопки."""
        self.growth_points += 1
        self.update_ui()

    def hire_gardener(self):
        """Найм садовника."""
        if self.growth_points >= self.gardener_cost:
            self.growth_points -= self.gardener_cost
            self.gardener_count += 1
            self.gardener_cost = int(self.gardener_cost * 1.4)  
            self.update_ui()

    def auto_grow(self):
        """Автоматический рост дерева благодаря садовникам."""
        self.growth_points += self.gardener_count * self.growth_per_gardener
        self.update_ui()

    def update_ui(self):
        """Обновление интерфейса."""
        self.growth_label.setText(f"Очки роста: {self.growth_points}")
        self.gardener_label.setText(
            f"Садовники: {self.gardener_count} (помогают расти на {self.gardener_count * self.growth_per_gardener} очков/сек)"
        )
        self.hire_button.setText(f"Нанять садовника - {self.gardener_cost} очков роста")


if __name__ == "__main__":
    app = QApplication([])

    window = TreeClicker()
    window.show()

    app.exec()
