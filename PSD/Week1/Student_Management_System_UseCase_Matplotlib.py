#!/usr/bin/env python3
"""
Student Management System - Use Case Diagram Generator (Matplotlib Version)
This script generates a use-case diagram showing actors and their use cases
using matplotlib instead of graphviz
"""

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.patches import FancyBboxPatch, ConnectionPatch
    import numpy as np
    print("✅ Matplotlib library found - generating use case diagram...")
except ImportError:
    print("❌ Matplotlib library not found. Installing...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.patches import FancyBboxPatch, ConnectionPatch
    import numpy as np
    print("✅ Matplotlib library installed successfully!")

def create_use_case_diagram():
    """Create a use case diagram for the Student Management System using matplotlib"""
    
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Define actors and their use cases
    actors = {
        'Student': ['Update Profile', 'Attend Class', 'Enroll Subject'],
        'Lecturer': ['Teach Class', 'Teach Subject', 'Grade Assignment'],
        'Admin': ['Design Timetable', 'Allocate Classrooms', 'Generate Reports']
    }
    
    # Colors
    actor_color = '#FFE6B3'  # Light orange
    use_case_color = '#B3D9FF'  # Light blue
    system_color = '#E6E6E6'  # Light gray
    
    # Draw system boundary
    system_boundary = FancyBboxPatch(
        (0.5, 0.5), 9, 9,
        boxstyle="round,pad=0.1",
        facecolor=system_color,
        edgecolor='black',
        linewidth=2,
        linestyle='--'
    )
    ax.add_patch(system_boundary)
    
    # Add system title
    ax.text(5, 9.5, 'Student Management System', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Position actors
    actor_positions = {
        'Student': (1, 8),
        'Lecturer': (5, 8),
        'Admin': (9, 8)
    }
    
    # Draw actors (stick figures)
    for actor, pos in actor_positions.items():
        # Actor box
        actor_box = FancyBboxPatch(
            (pos[0]-0.4, pos[1]-0.3), 0.8, 0.6,
            boxstyle="round,pad=0.05",
            facecolor=actor_color,
            edgecolor='black',
            linewidth=1.5
        )
        ax.add_patch(actor_box)
        
        # Actor label
        ax.text(pos[0], pos[1], actor, 
                fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Draw use cases
    use_case_positions = {}
    use_case_id = 1
    
    for actor, use_cases in actors.items():
        base_x = actor_positions[actor][0]
        base_y = 6.5
        
        for i, use_case in enumerate(use_cases):
            # Calculate position for this use case
            if len(use_cases) == 3:
                if i == 0:  # First use case
                    x = base_x - 0.8
                    y = base_y + 0.5
                elif i == 1:  # Second use case
                    x = base_x
                    y = base_y
                else:  # Third use case
                    x = base_x + 0.8
                    y = base_y + 0.5
            else:
                x = base_x + (i - 1) * 0.8
                y = base_y
            
            use_case_positions[f'UC{use_case_id:02d}'] = (x, y, use_case)
            
            # Draw use case ellipse
            use_case_ellipse = patches.Ellipse(
                (x, y), 1.2, 0.6,
                facecolor=use_case_color,
                edgecolor='black',
                linewidth=1.5
            )
            ax.add_patch(use_case_ellipse)
            
            # Use case label
            ax.text(x, y, use_case, 
                    fontsize=9, fontweight='bold', ha='center', va='center',
                    wrap=True)
            
            use_case_id += 1
    
    # Draw connections (lines from actors to use cases)
    for actor, use_cases in actors.items():
        actor_pos = actor_positions[actor]
        
        for i, use_case in enumerate(use_cases):
            # Find the corresponding use case position
            for uc_id, (uc_x, uc_y, uc_name) in use_case_positions.items():
                if uc_name == use_case:
                    # Draw line from actor to use case
                    line = ConnectionPatch(
                        (actor_pos[0], actor_pos[1] - 0.3),  # From actor bottom
                        (uc_x, uc_y + 0.3),  # To use case top
                        "data", "data",
                        arrowstyle="->",
                        shrinkA=5,
                        shrinkB=5,
                        mutation_scale=20,
                        fc="black",
                        linewidth=1.5
                    )
                    ax.add_patch(line)
                    break
    
    # Add legend
    legend_elements = [
        patches.Patch(color=actor_color, label='Actors'),
        patches.Patch(color=use_case_color, label='Use Cases'),
        patches.Patch(color=system_color, label='System Boundary')
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0.02, 0.98))
    
    # Set title
    plt.suptitle('Student Management System - Use Case Diagram', 
                 fontsize=18, fontweight='bold', y=0.95)
    
    return fig

def save_diagram(fig, filename='student_management_use_case_diagram'):
    """Save the diagram to files"""
    try:
        # Save as PNG
        fig.savefig(f'{filename}.png', dpi=300, bbox_inches='tight')
        print(f"✅ Use case diagram saved as '{filename}.png'")
        
        # Save as PDF
        fig.savefig(f'{filename}.pdf', bbox_inches='tight')
        print(f"✅ Use case diagram saved as '{filename}.pdf'")
        
        # Save as SVG
        fig.savefig(f'{filename}.svg', bbox_inches='tight')
        print(f"✅ Use case diagram saved as '{filename}.svg'")
        
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
    print("🎓 STUDENT MANAGEMENT SYSTEM - USE CASE DIAGRAM GENERATOR (MATPLOTLIB)")
    print("=" * 60)
    
    try:
        # Create the diagram
        fig = create_use_case_diagram()
        
        # Print summary
        print_use_case_summary()
        
        # Save the diagram
        save_diagram(fig)
        
        print("\n🎉 Use case diagram generated successfully!")
        print("\nFiles created:")
        print("  - student_management_use_case_diagram.png (high-resolution PNG)")
        print("  - student_management_use_case_diagram.pdf (PDF format)")
        print("  - student_management_use_case_diagram.svg (scalable vector)")
        
        print("\n💡 To view the diagram:")
        print("  - Open the PNG file in any image viewer")
        print("  - Open the PDF file in any PDF reader")
        print("  - Open the SVG file in any web browser or vector editor")
        
        # Show the diagram (optional)
        print("\n🖼️  Displaying diagram... (close window to continue)")
        plt.show()
        
    except Exception as e:
        print(f"\n❌ Error generating use case diagram: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
