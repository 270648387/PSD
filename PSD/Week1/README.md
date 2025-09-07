# 🎓 Student Management System - Use Case Diagram Generator

This Python script generates a professional use-case diagram for a Student Management System, showing the three main actors and their respective use cases.

## 📋 Actors and Use Cases

### 👤 Student
1. **Update Profile** - Modify personal information and preferences
2. **Attend Class** - Participate in scheduled classes
3. **Enroll Subject** - Register for academic courses

### 👨‍🏫 Lecturer
1. **Teach Class** - Conduct classroom sessions
2. **Teach Subject** - Deliver course content
3. **Grade Assignment** - Evaluate student submissions

### 👨‍💼 Admin
1. **Design Timetable** - Create and manage class schedules
2. **Allocate Classrooms** - Assign rooms to classes
3. **Generate Reports** - Create system analytics and reports

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Graphviz system package (see installation notes below)

### Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Graphviz system package:**
   
   **Windows:**
   - Download from [https://graphviz.org/download/](https://graphviz.org/download/)
   - Add to PATH environment variable
   
   **macOS:**
   ```bash
   brew install graphviz
   ```
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt-get install graphviz
   ```
   
   **CentOS/RHEL:**
   ```bash
   sudo yum install graphviz
   ```

### Usage

Run the script to generate the use case diagram:

```bash
python Student_Management_System_UseCase.py
```

## 📁 Output Files

The script generates three file formats:

1. **`student_management_use_case_diagram.png`** - Visual diagram (PNG format)
2. **`student_management_use_case_diagram.pdf`** - High-quality PDF format
3. **`student_management_use_case_diagram.dot`** - Graphviz source code

## 🎨 Diagram Features

- **Clear Actor Representation** - Each actor is clearly labeled and positioned
- **Use Case Ellipses** - All use cases are displayed as ovals with descriptive names
- **System Boundary** - Dashed rectangle showing the system scope
- **Professional Styling** - Color-coded nodes for better readability
- **Multiple Formats** - Export to PNG, PDF, and DOT formats

## 🔧 Customization

You can easily modify the script to:

- Add new actors and use cases
- Change colors and styling
- Modify the layout and positioning
- Add relationships between use cases
- Include system boundaries and packages

## 📊 Example Output

The generated diagram will show:
- 3 Actors (Student, Lecturer, Admin)
- 9 Use Cases (3 per actor)
- Clear connections between actors and their use cases
- Professional UML-style formatting

## 🐛 Troubleshooting

### Common Issues:

1. **Graphviz not found:**
   - Ensure Graphviz system package is installed
   - Check PATH environment variable (Windows)

2. **Python graphviz library error:**
   - Run: `pip install graphviz`
   - Verify Python version compatibility

3. **Permission errors:**
   - Ensure write permissions in the current directory
   - Run as administrator if needed (Windows)

## 📚 Additional Resources

- [Graphviz Documentation](https://graphviz.org/documentation/)
- [UML Use Case Diagrams](https://www.uml-diagrams.org/use-case-diagrams.html)
- [Python Graphviz Library](https://pypi.org/project/graphviz/)

## 🤝 Contributing

Feel free to enhance this script by:
- Adding more use case relationships
- Implementing include/extend relationships
- Adding more diagram styling options
- Supporting additional export formats

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Diagramming! 🎨📊**
