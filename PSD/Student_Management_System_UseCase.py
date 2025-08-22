#!/usr/bin/env python3
"""
Student Management System - Use Case Diagram Generator
This script generates a use-case diagram showing actors and their use cases
"""

try:
    from graphviz import Digraph
    print("✅ Graphviz library found - generating use case diagram...")
except ImportError:
    print("❌ Graphviz library not found. Installing...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "graphviz"])
    from graphviz import Digraph
    print("✅ Graphviz library installed successfully!")

def create_use_case_diagram():
    """Create a use case diagram for the Student Management System"""
    
    # Create the diagram
    dot = Digraph(comment='Student Management System - Use Case Diagram')
    dot.attr(rankdir='TB')
    
    # Set graph attributes
    dot.attr('node', shape='ellipse', style='filled', fillcolor='lightblue')
    
    # Define actors
    actors = {
        'Student': ['Update Profile', 'Attend Class', 'Enroll Subject'],
        'Lecturer': ['Teach Class', 'Teach Subject', 'Grade Assignment'],
        'Admin': ['Design Timetable', 'Allocate Classrooms', 'Generate Reports']
    }
    
    # Add use case nodes
    use_case_id = 1
    for actor, use_cases in actors.items():
        for use_case in use_cases:
            node_id = f'UC{use_case_id:02d}'
            dot.node(node_id, use_case)
            use_case_id += 1
    
    # Add actor nodes (stick figures)
    dot.attr('node', shape='rectangle', style='filled', fillcolor='lightgreen')
    dot.node('Student', 'Student')
    dot.node('Lecturer', 'Lecturer')
    dot.node('Admin', 'Admin')
    
    # Connect actors to their use cases
    use_case_id = 1
    for actor, use_cases in actors.items():
        for use_case in use_cases:
            node_id = f'UC{use_case_id:02d}'
            dot.edge(actor, node_id)
            use_case_id += 1
    
    # Add system boundary
    dot.attr('node', shape='rectangle', style='dashed', fillcolor='white', label='')
    dot.node('System', 'Student Management System')
    
    return dot

def save_diagram(dot, filename='student_management_use_case_diagram'):
    """Save the diagram to a file"""
    try:
        # Save as PNG
        dot.render(filename, format='png', cleanup=True)
        print(f"✅ Use case diagram saved as '{filename}.png'")
        
        # Save as PDF
        dot.render(filename, format='pdf', cleanup=True)
        print(f"✅ Use case diagram saved as '{filename}.pdf'")
        
        # Save as DOT file (source)
        dot.save(f"{filename}.dot")
        print(f"✅ Use case diagram source saved as '{filename}.dot'")
        
    except Exception as e:
        print(f"❌ Error saving diagram: {e}")

def print_use_case_summary():
    """Print a summary of the use cases"""
    print("\n" + "=" * 60)
    print("STUDENT MANAGEMENT SYSTEM - USE CASE SUMMARY")
    print("=" * 60)
    
    actors = {
        'Student': ['Update Profile', 'Attend Class', 'Enroll Subject'],
        'Lecturer': ['Teach Class', 'Teach Subject', 'Grade Assignment'],
        'Admin': ['Design Timetable', 'Allocate Classrooms', 'Generate Reports']
    }
    
    for actor, use_cases in actors.items():
        print(f"\n👤 {actor}:")
        for i, use_case in enumerate(use_cases, 1):
            print(f"   {i}. {use_case}")
    
    print("\n" + "=" * 60)
    print("Total Actors: 3")
    print("Total Use Cases: 9")
    print("=" * 60)

def main():
    """Main function to generate the use case diagram"""
    print("🎓 STUDENT MANAGEMENT SYSTEM - USE CASE DIAGRAM GENERATOR")
    print("=" * 60)
    
    try:
        # Create the diagram
        dot = create_use_case_diagram()
        
        # Print summary
        print_use_case_summary()
        
        # Save the diagram
        save_diagram(dot)
        
        print("\n🎉 Use case diagram generated successfully!")
        print("\nFiles created:")
        print("  - student_management_use_case_diagram.png (visual diagram)")
        print("  - student_management_use_case_diagram.pdf (PDF format)")
        print("  - student_management_use_case_diagram.dot (source code)")
        
        print("\n💡 To view the diagram:")
        print("  - Open the PNG file in any image viewer")
        print("  - Open the PDF file in any PDF reader")
        print("  - Use Graphviz tools to render the DOT file")
        
    except Exception as e:
        print(f"\n❌ Error generating use case diagram: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
