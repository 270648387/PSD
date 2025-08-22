#!/usr/bin/env python3
"""
Student Management System - Use Case Diagram Generator
Master script to run all versions
"""

import os
import sys

def print_banner():
    """Print the application banner"""
    print("🎓" + "=" * 60)
    print("STUDENT MANAGEMENT SYSTEM - USE CASE DIAGRAM GENERATOR")
    print("=" * 60)
    print("Choose your preferred version:")

def print_menu():
    """Print the main menu"""
    print("\n📋 AVAILABLE VERSIONS:")
    print("1. 🖼️  Graphviz Version (Professional visual diagrams)")
    print("2. 🎨 Matplotlib Version (High-quality visual diagrams)")
    print("3. 📝 Text Version (Console-based display)")
    print("4. 🚀 Run All Versions")
    print("5. 📊 View Generated Files")
    print("0. 🚪 Exit")
    print("-" * 60)

def run_graphviz_version():
    """Run the Graphviz version"""
    print("\n🖼️  Running Graphviz Version...")
    print("-" * 40)
    
    try:
        if os.path.exists("Student_Management_System_UseCase.py"):
            os.system("python Student_Management_System_UseCase.py")
        else:
            print("❌ Graphviz version file not found!")
    except Exception as e:
        print(f"❌ Error running Graphviz version: {e}")

def run_matplotlib_version():
    """Run the Matplotlib version"""
    print("\n🎨 Running Matplotlib Version...")
    print("-" * 40)
    
    try:
        if os.path.exists("Student_Management_System_UseCase_Matplotlib.py"):
            os.system("python Student_Management_System_UseCase_Matplotlib.py")
        else:
            print("❌ Matplotlib version file not found!")
    except Exception as e:
        print(f"❌ Error running Matplotlib version: {e}")

def run_text_version():
    """Run the Text version"""
    print("\n📝 Running Text Version...")
    print("-" * 40)
    
    try:
        if os.path.exists("Student_Management_System_UseCase_Text.py"):
            os.system("python Student_Management_System_UseCase_Text.py")
        else:
            print("❌ Text version file not found!")
    except Exception as e:
        print(f"❌ Error running Text version: {e}")

def run_all_versions():
    """Run all versions sequentially"""
    print("\n🚀 Running All Versions...")
    print("=" * 60)
    
    print("\n1️⃣  Running Graphviz Version...")
    run_graphviz_version()
    
    print("\n2️⃣  Running Matplotlib Version...")
    run_matplotlib_version()
    
    print("\n3️⃣  Running Text Version...")
    run_text_version()
    
    print("\n🎉 All versions completed!")

def view_generated_files():
    """Show all generated files"""
    print("\n📊 Generated Files:")
    print("-" * 40)
    
    files_to_check = [
        "student_management_use_case_diagram.png",
        "student_management_use_case_diagram.pdf",
        "student_management_use_case_diagram.svg",
        "student_management_use_case_diagram.dot"
    ]
    
    found_files = []
    for file in files_to_check:
        if os.path.exists(file):
            size = os.path.getsize(file)
            size_kb = size / 1024
            print(f"✅ {file} ({size_kb:.1f} KB)")
            found_files.append(file)
        else:
            print(f"❌ {file} (not found)")
    
    if not found_files:
        print("\n💡 No diagram files found yet. Run one of the diagram generators first!")
    else:
        print(f"\n📁 Total files found: {len(found_files)}")
        print("\n💡 To view the diagrams:")
        print("   - PNG/SVG: Open in any image viewer or web browser")
        print("   - PDF: Open in any PDF reader")
        print("   - DOT: Use Graphviz tools or online viewers")

def check_dependencies():
    """Check if required dependencies are available"""
    print("\n🔍 Checking Dependencies...")
    print("-" * 40)
    
    dependencies = {
        "Graphviz": "graphviz",
        "Matplotlib": "matplotlib",
        "NumPy": "numpy"
    }
    
    available = {}
    for name, package in dependencies.items():
        try:
            __import__(package)
            available[name] = True
            print(f"✅ {name}: Available")
        except ImportError:
            available[name] = False
            print(f"❌ {name}: Not available")
    
    return available

def install_dependencies():
    """Install missing dependencies"""
    print("\n📦 Installing Dependencies...")
    print("-" * 40)
    
    try:
        os.system("pip install -r requirements_all.txt")
        print("✅ Dependencies installed successfully!")
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")

def main():
    """Main function"""
    print_banner()
    
    # Check dependencies
    deps = check_dependencies()
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-5): ").strip()
            
            if choice == "0":
                print("\n👋 Thank you for using the Use Case Diagram Generator!")
                break
            elif choice == "1":
                if deps.get("Graphviz", False):
                    run_graphviz_version()
                else:
                    print("❌ Graphviz not available. Install dependencies first.")
                    install_dependencies()
            elif choice == "2":
                if deps.get("Matplotlib", False):
                    run_matplotlib_version()
                else:
                    print("❌ Matplotlib not available. Install dependencies first.")
                    install_dependencies()
            elif choice == "3":
                run_text_version()
            elif choice == "4":
                run_all_versions()
            elif choice == "5":
                view_generated_files()
            else:
                print("❌ Invalid choice. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
