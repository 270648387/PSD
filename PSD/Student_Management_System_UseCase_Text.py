def print_use_case_diagram():
    """Print a text-based use case diagram"""
    
    print("🎓 STUDENT MANAGEMENT SYSTEM - USE CASE DIAGRAM")
    print("=" * 80)
    print()
    
    # System boundary
    print("STUDENT MANAGEMENT SYSTEM")
    print()
    
    # Actors and their use cases
    actors = {
        'Student': ['Update Profile', 'Attend Class', 'Enroll Subject'],
        'Lecturer': ['Teach Class', 'Teach Subject', 'Grade Assignment'],
        'Admin': ['Design Timetable', 'Allocate Classrooms', 'Generate Reports']
    }
    
    # Print actors and use cases
    for actor, use_cases in actors.items():
        print(f"{actor}")
        print("   │")
        
        for i, use_case in enumerate(use_cases):
            if i == len(use_cases) - 1:  # Last use case
                print(f"   └─── {use_case}")
            else:
                print(f"   ├─── {use_case}")
        
        print()
    
    # Print summary
    print("=" * 80)
    print("DIAGRAM SUMMARY")
    print(f"\nTotal Actors: {len(actors)}")
    print(f"Total Use Cases: {sum(len(use_cases) for use_cases in actors.values())}")
    print()
    
    # Print detailed use case descriptions
    print("=" * 80)
    print("USE CASE DESCRIPTIONS")
    
    use_case_descriptions = {
        'Update Profile': 'Modify personal information, contact details, and preferences',
        'Attend Class': 'Participates in scheduled classroom sessions',
        'Enroll Subject': 'Registers for academic courses and modules',
        'Teach Class': 'Lecturer teach classes',
        'Teach Subject': 'Lecturer is responsible for course delivery and curriculum',
        'Grade Assignment': 'Evaluates and provides feedback on student assessments',
        'Design Timetable': 'Creates and manages class schedules and time slots',
        'Allocate Classrooms': 'Assigns physical rooms to classes and sessions',
        'Generate Reports': 'Creates system analytics and administrative reports'
    }
    
    for use_case, description in use_case_descriptions.items():
        print(f"{use_case}")
        print(f"   {description}")
        print()


def main():
    """Main function to display the use case diagram"""
    
    try:
        # Display the main use case diagram
        print_use_case_diagram()
        
        print("Use case diagram displayed successfully!")
        print("\nThis text-based diagram shows:")
        print("   - All actors and their use cases")
        print("   - Clear relationships between actors and use cases")
        print("   - Detailed descriptions of each use case")
        
    except Exception as e:
        print(f"\nError displaying use case diagram: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
