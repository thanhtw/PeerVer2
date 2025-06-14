"""
English translations for Java Peer Review Training System.

This module provides English translations for the UI and system messages.
"""

# LLM instructions for responding in English
llm_instructions = """
Please respond in English. Use clear, concise language appropriate for programming education.
Format code examples, error explanations, and feedback in a way that's easy to understand for 
programming students.
"""

# English translations
translations = {
    # General
    "about": "About",
    "about_app": "This application helps you learn and practice Java code review skills by generating code with intentional errors for you to identify.",
    "app_subtitle": "Learn and practice Java code review skills with AI-generated exercises",
    "app_title": "Java Code Review Training System",
    "current_language": "Current Language",
    
    # Login/Register
    "confirm_password": "Confirm Password",
    "continue_demo": "Continue in Demo Mode (No Login Required)",
    "demo_mode": "Demo Mode",
    "display_name": "Display Name",
    "email": "Email",
    "email_in_use": "Email already in use",
    "experience_level": "Your Experience Level",
    "fill_all_fields": "Please fill in all fields",
    "hi": "Hi",
    "invalid_credentials": "Invalid email or password",
    "level": "Your level",
    "login": "Login",
    "login_failed": "Login failed",
    "password": "Password",
    "passwords_mismatch": "Passwords do not match",
    "register": "Register",
    "registration_failed": "Registration failed",
    "review_times": "Review Times",
    "score": "Your Score",
    
    # Provider sections
    "api_key_required": "API key is required for Groq",        
    "groq_api_key": "Groq API Key ",
    "groq_api_message": "Groq API uses cloud-hosted models and requires an API key",
    "groq_mode": "Groq API (Cloud)",
    "llm_provider_setup": "LLM Provider Setup",
    "not_connected_to_groq": "Not connected to Groq API",   
    
    # Code Generation
    "added": "Added",
    "advanced_mode": "Advanced: Select by error categories",
    "advanced_mode_help": "Advanced Mode: Select specific error categories to include in the generated code. The system will randomly choose errors from your selected categories.",
    "all_errors_implemented": "All requested errors successfully implemented!",
    "attempts": "attempts",
    "category": "Category",
    "code_exists_but_empty": "Code snippet exists but contains no code. Please try regenerating the code.",
    "code_generation_complete": "Code generation complete! Proceeding to review tab...",
    "code_generation_completed": "Code generation process completed successfully",
    "code_generation_process": "Code Generation Process",
    "code_length": "Code Length",
    "code_params": "Code Parameters (Based on Your Level)",
    "code_quality": "Code Quality",
    "completed": "completed",
    "difficulty": "Difficulty Level",
    "easy": "Easy",
    "error_categories": "Error Categories",
    "error_details": "Error Details",
    "error_selection_mode": "Error Selection Mode",
    "error_selection_prompt": "How would you like to select errors?",
    "errors_found": "Errors Found",
    "evaluated_code": "Evaluated code for requested errors",
    "evaluating_code": "Evaluating generated code for errors...",
    "found": "Found",
    "generate_code_button": "Generate Code Problem",
    "generate_new": "Generate New Problem",
    "generate_problem": "Generate Java Code Review Problem",
    "generated_initial_code": "Generated initial code",
    "generated_java_code": "Generated Java Code",
    "generating_code": "Generating and evaluating code...",
    "generation_attempts": "Generation Attempts",
    "generation_stats": "Generation Stats",
    "good_quality": "Good quality code generated with",
    "hard": "Hard",
    "improving_code": "Improving code quality",
    "long": "Long",
    "medium": "Medium",
    "new_errors": "new errors in this attempt!",
    "no_categories": "No categories selected. You must select at least one category to generate code.",
    "no_code_generated": "No code has been generated yet. Please go to the 'Generate Problem' tab first.",
    "no_code_generated_use_generate": "No code generated yet. Use the 'Generate Problem' tab to create a Java code snippet.",
    "no_code_snippet_available": "No code snippet available",
    "no_code_snippet_evaluation": "No code snippet available for evaluation",
    "no_errors_found": "No errors found in",
    "no_process_details": "No process details available.",
    "no_specific_issues": "No specific issue selected. Random errors will be used based on categories.",
    "params_based_on_level": "These parameters are automatically set based on your experience level",
    "partial_quality": "Code generated with",
    "process_details": "Process Details",
    "quality": "Quality",
    "reevaluated_code": "Re-evaluated regenerated code",
    "reevaluating_code": "Re-evaluating code...",
    "regenerating_code": "Regenerating code",
    "remove": "Remove",
    "select": "Select",
    "select_error_categories": "Select Error Categories",
    "select_specific_errors": "Select Specific Errors",
    "selected": "Selected",
    "selected_categories": "Selected Categories",
    "selected_issues": "Selected Issues",
    "short": "Short",
    "specific_mode": "Specific: Choose exact errors to include",
    "start_process": "Started code generation process",
    "starting_new_session": "Starting a new code review session. Please configure and generate a new problem.",
    "step1": "1. Generate Code",
    "step2": "2. Evaluate Code",
    "step3": "3. Regenerate",
    "step4": "4. Ready for Review",
    "workflow_not_initialized": "Workflow state not initialized. Please refresh the page.",
    
    # Review
    "all_errors_found": "🎉 Congratulations! You've found all the errors! Proceed to the feedback tab to see your results.",
    "analysis_complete": "Analysis complete! Displaying results...",
    "analyzing_review": "Analyzing your review...",
    "array_handling_category": "array handling",
    "attempt": "Attempt",
    "be_comprehensive": "Be Comprehensive: Look for different types of issues",
    "be_constructive": "Be Constructive: Suggest improvements, not just criticisms",
    "be_specific": "Be Specific: Point out exact lines or areas where problems occur",
    "check_for": "Check for:",
    "clear": "Clear",
    "code_formatting_category": "code formatting",
    "code_style_formatting": "Code style and formatting issues",
    "documentation_completeness": "Documentation completeness",
    "efficiency_performance": "Efficiency and performance concerns",
    "enter_review": "Enter your review comments here",
    "example_review_comment1": "Line 15: The variable name 'cnt' is too short and unclear. It should be renamed to something more descriptive like 'counter'.",
    "example_review_comment2": "Line 27: This loop will miss the last element because it uses < instead of <=",
    "example_review_comment3": "Line 42: The string comparison uses == instead of .equals() which will compare references not content",
    "example_review_comment4": "Line 72: Missing null check before calling method on user object",
    "exception_handling_category": "exception handling",
    "format_your_review": "Format Your Review",
    "formal_categories_note": "You don't need to use formal error categories - writing in natural language is perfect!",
    "how_to_write": "How to Write an Effective Code Review:",
    "iteration": "Iteration",
    "iterations_completed": "You have completed all {max_iterations} review iterations. View feedback in the next tab.",
    "logical_error_category": "logical error",
    "logical_errors_bugs": "Logical errors and bugs",
    "naming_convention_category": "naming convention",
    "naming_conventions": "Naming conventions and coding standards",
    "null_pointer_category": "null pointer",
    "object_comparison_category": "object comparison",
    "please_enter_review": "Please enter your review before submitting",
    "please_generate_problem_first": "Please generate a code problem first",
    "previous_results": "Previous Results",
    "previous_review": "Previous Review",
    "processing_review": "Processing your review...",
    "review_cannot_be_empty": "Review cannot be empty",
    "review_example": "Examples of Good Review Comments:",
    "review_format_example": "Line X: Description of the issue and why it's problematic",
    "review_guidance": "Review Guidance",
    "review_guidelines": "Review Guidelines",
    "review_help_text": "Provide detailed feedback on the code. Be specific about line numbers and issues you've identified.",
    "review_history": "Review History",
    "review_java_code": "Review Java Code",
    "review_placeholder": "Example:\nLine 15: The variable 'cnt' uses poor naming. Consider using 'counter' instead.\nLine 27: The loop condition should use '<=' instead of '<' to include the boundary value.",
    "review_process_complete": "Review process complete, switching to feedback tab",
    "security_vulnerabilities": "Potential security vulnerabilities",
    "submit_review": "Submit Your Code Review",
    "submit_review_button": "Submit Review",
    "syntax_compilation_errors": "Syntax and compilation errors",
    "try_find_more_issues": "Try to find more issues in this attempt.",
    "view_feedback": "View Feedback",
    "you_identified": "You identified",
    "your_review": "Your Review",
    
    # Feedback
    "accuracy": "Accuracy",
    "accuracy_percentage": "Accuracy Percentage",
    "all_issues_found": "Great job! You found all the issues!",
    "check_detailed_analysis": "Check the detailed analysis in the comparison report for more information.",
    "check_review_history": "Please check your review history for details",
    "complete_review_first": "Please complete all review attempts before accessing feedback.",
    "congratulations": "Congratulations",
    "correctly_identified_issues": "Correctly Identified Issues",
    "current_process_review1": "Current progress",
    "current_process_review2": "attempts completed",
    "default_feedback": "The system was unable to extract detailed feedback. Please check the overall analysis results.",
    "detailed_analysis": "Detailed Analysis",
    "educational_feedback": "Educational Feedback:",
    "error_generating_report": "There was an error generating a detailed comparison report.",
    "excellent_work_guidance": "Excellent work! Try to be even more specific in your explanations of why each issue is problematic.",
    "false_positives": "False Positives",
    "feedback": "Feedback",
    "generated_comparison_report": "Generated comparison report for feedback tab",
    "generating_comparison_report": "generating comparison report",
    "good_performance_guidance": "You're doing well! Try looking for issues related to '{missed_text}'. Check for similar patterns elsewhere in the code.",
    "hint": "hint",
    "identified_count": "Identified Count",
    "identified_issues": "Identified Issues",
    "identified_percentage": "Identified Percentage",
    "identified_problems": "Identified Problems",
    "issues": "issues",
    "issues_found": "Issues Found",
    "issues_identified": "Issues Identified",
    "issues_missed": "Issues You Missed",
    "issues_you_missed": "Issues You Missed",
    "level_upgraded": "Your level has been upgraded from",
    "low_performance_guidance": "Try a more systematic approach: first check variable declarations, then method signatures, then control flow statements. Look specifically for naming conventions and null handling.",
    "max_iterations": "Max Iterations",
    "medium_performance_general_guidance": "You've found some issues but missed others. Be more methodical - check each line, method signature, and variable declaration carefully.",
    "medium_performance_guidance": "Look more carefully for {category} issues. Compare variable types, check method names, and examine control flow statements.",
    "missed_issues": "Missed Issues",
    "missed_problems": "Missed Problems",
    "new_session": "Ready for another review?",
    "new_session_desc": "Start a new code review session to practice with different errors.",
    "no_analysis_results": "No analysis results available. Please submit your review in the 'Submit Review' tab first.",
    "no_identified_issues": "You didn't identify any issues correctly.",
    "no_result_returned": "No result returned",
    "overall_accuracy": "Overall Accuracy",
    "problem": "Problem",
    "progress_across_iterations": "Progress Across Iterations",
    "remaining_attempts": "Remaining Attempts",
    "review_completed_all_identified": "Review completed: all",
    "review_completed_max_iterations": "Review completed: max iterations reached",
    "review_completed_sufficient": "Review completed: sufficient review",
    "review_performance_summary": "Review Performance Summary",
    "review_sufficient": "Review Sufficient",
    "start_new_session": "Start New Session",
    "statistics_updated": "Statistics updated",    
    "student_comment": "Student Comment",
    "successfully_updated_statistics": "Successfully updated user statistics",
    "targeted_guidance": "Targeted Guidance",
    "to": "to",
    "to_your_score": "to your score",
    "total_problems": "Total Problems",
    "unknown_error": "Unknown error",
    "updating_statistics": "updating statistics",
    "updating_user_statistics": "updating user statistics",
    "your_final_review": "Your Final Review (Attempt {iteration})",
    
    # Tabs
    "tab_feedback": "3. View Feedback",
    "tab_generate": "1. Generate Problem",
    "tab_logs": "4. LLM Logs",
    "tab_review": "2. Submit Review",
    
    # Error categories
    "code_quality": "Code Quality",
    "code_quality_desc": "Style, readability, and maintainability issues",
    "java_specific": "Java Specific",
    "java_specific_desc": "Issues specific to Java language features",
    "logical": "Logical",
    "logical_desc": "Issues with program logic, calculations, and flow control",
    "standard_violation": "Standard Violation",
    "standard_violation_desc": "Violations of Java conventions and best practices",
    "syntax": "Syntax",
    "syntax_desc": "Java language syntax and structure errors",
    
    # Language selection
    "chinese": "Traditional Chinese",
    "english": "English",
    "language": "Language",
    
    # LLM logs
    "clear_logs": "Clear Logs",
    "clear_logs_warning": "This will remove in-memory logs. Log files on disk will be preserved.",
    "confirm_clear_logs": "Confirm Clear Logs",
    "displaying_logs": "Displaying {count} recent logs. Newest logs appear first.",
    "filter_by_date": "Filter by date:",
    "filter_by_type": "Filter by log type:",
    "llm_logger_not_initialized": "LLM logger not initialized.",
    "llm_logs_title": "LLM Interaction Logs",
    "log_info_markdown": """
    ### Log Information

    Log files are stored in the `llm_logs` directory, with subdirectories for each interaction type:

    - code_generation
    - code_regeneration
    - code_evaluation
    - review_analysis
    - summary_generation

    Each log is stored as both a `.json` file (for programmatic use) and a `.txt` file (for easier reading).
    """,
    "logs_cleared": "Logs cleared.",
    "logs_to_display": "Number of logs to display",
    "metadata_tab": "Metadata",
    "no_logs_found": "No logs found. Generate code or submit reviews to create log entries.",
    "no_logs_match": "No logs match the selected filters.",
    "no_metadata": "No metadata available",
    "no_response": "No response available",
    "prompt_sent": "Prompt sent to LLM:",
    "prompt_tab": "Prompt",
    "refresh_logs": "Refresh Logs",
    "response_label": "Response:",
    "response_tab": "Response",
    "unknown_time": "Unknown time",
    "unknown_type": "Unknown type",

    "troubleshooting": "Troubleshooting",
    
    # Error messages
    "analysis_could_not_extract_feedback": "The analysis could not extract feedback.",
    "could_not_extract_analysis_data": "Could not extract analysis data from LLM response",
    "could_not_extract_json": "Could not extract JSON, attempting manual extraction",
    "could_not_parse_json_response": "Could not parse JSON response",
    "empty_response_from_llm": "Empty response from LLM",
    "error": "error",
    "error_extracting_json": "Error extracting JSON",
    "error_generating_guidance": "Error generating guidance with LLM",
    "failed_update_statistics": "Failed to update statistics",
    "generating_concise_targeted_guidance": "Generating concise targeted guidance for iteration {iteration_count}",
    "iteration_count": "Iteration Count",
    "json_parse_error": "JSON parsing error",
    "no_llm_provided_for_guidance": "No LLM provided for guidance generation, using concise fallback guidance",
    "no_review_submitted": "No review submitted to analyze",
    "no_specific_errors_selected": "No specific errors selected. Please select at least one error before generating code.",
    "preparing_update_stats": "Preparing to update stats",
    "raw_text": "raw_text",
    "student_evaluator_not_initialized": "Student response evaluator not initialized",
    "trimmed_guidance_words": "Trimmed guidance from {before} to {after} words",


    # Code generator log messages
    "generating_java_code_with_provider": "Generating Java code with provider: {provider}",
    "generating_java_code_with_groq": "Generating Java code with Groq model: {model}",
    "generating_java_code_with_llm": "Generating Java code with LLM: {length} length, {difficulty} difficulty, {domain} domain",
    "llm_response_type": "LLM response type: {type}",
    "error_generating_code_with_llm": "Error generating code with LLM: {error}",
    "provider": "provider",

    # Code evaluation messages
    "please_ensure_code_contains_all": "Please ensure the code contains all",
    "requested_errors": "requested errors",
    "sending_code_to_llm_for_evaluation": "Sending code to LLM for evaluation",   
    "extracting_json_from_response": "Extracting JSON from response",
    "could_not_convert_response_to_string": "Could not convert response to string",
    "using_manually_extracted_errors": "Using manually extracted errors",
    "could_not_extract_json_from_response": "Could not extract JSON from response, returning default structure",
    "extraction_failed": "EXTRACTION_FAILED",
    "could_not_extract_proper_analysis": "Could not extract proper analysis from model response.",
    "received_none_result": "Received None result in _process_evaluation_result",
    "failed_to_process_evaluation_result": "Failed to process evaluation result",
    "expected_dict_for_result": "Expected dict for result, got",
    "got": "got",
    "invalid_evaluation_result_type": "Invalid evaluation result type",
    "is_not_a_list": "is not a list, got",
    "skipping_non_dict_error": "Skipping non-dict error in requested_errors",
    "could_not_process_non_dict_error": "Could not process non-dict error",
    "all": "All",
    "requested_errors_are_properly_implemented": "requested errors are properly implemented",
    "out_of": "out of",
    "missing": "missing",
    "errors": "errors",
    "found": "Found",
    "error_type": "Error Type",
    "error_name":"Error Name",
    "line_number": "Line Number",
    "explanation": "Expanation",
    "valid": "Valid",
    "code_segment": "Code Segment",
    "name":"name",
    "error_name_variable":"error_name",
    "description":"description",
    "implementation_guide":"implementation_guide",
    "requested_errors":"requested_errors",
    "missing_errors":"missing_errors",
    "found_errors":"found_errors",
    "domain":"domain",
    "attempt":"attempt",
    "line_X_invalid_format": "Line {line} does not follow the required format.",
    "lines_X_invalid_format": "Lines {lines} do not follow the required format.",
    "please_use_format_line_description": "Please use the format 'Line X: description of problem' for each issue you identify.",
    "no_review_history_found": "No review history found.",
    "iteration_number":"Iteration Number",
    "review_analysis":"Review Analysis",
    "original_error_count": "Original Error Count",
    "comparison_report": "Comparison Report",
    "Meaningfulness" : "Meaningfulness",
    "meaningful_comments":"Meaningful Comments",
    "example": "Example",

    "rank": "Rank",
    "user": "User",
    "level": "Level",
    "points": "Points",
    "badges": "Badges",
    "leaderboard": "Leaderboard",
    "no_users_leaderboard": "No users on the leaderboard yet!",    
    
    "progress": "Progress",
   


    # Achievement badges section
    "achievement_badges": "Achievement Badges",
    "no_badges_earned": "No badges earned yet. Complete reviews to earn badges!",

    # Progress dashboard labels
    "progress_dashboard": "Progress Dashboard",
    "no_progress_data": "Complete more reviews to see your progress across error categories!",
    "error_category_mastery": "Error Category Mastery",
    "category": "Category",
    "mastery_level": "Mastery Level (%)",
    "errors_encountered_vs_identified": "Errors Encountered vs Identified",
    "encountered": "Encountered", 
    "identified": "Identified",
    "count": "Count",
    "skill_tree": "Skill Tree",
    "overall_mastery": "Overall Mastery",
    "java_review_skills": "Java Review Skills",
    "your_rank": "Your rank: {rank} of {total} users",
    "unknown": "Unknown",
    "basic": "Basic",
    "medium": "Medium",
    "senior": "Senior",
    "specify_different_names_per_language": "Specify different names for each language",
    "english_name": "English Name",
    "chinese_name": "Chinese Name", 
    "registration_success": "Registration successful!",
    "login_success": "Login successful!",
    "login_to_see":"Login to view the leaderboard!",

    # Add to the translations dictionary
    "Java Code Review Tutorial": "Java Code Review Tutorial",
    "1stPractice": "Your First Practice with Code Review in Our System",
    "Welcome to the Java Code Review Training System! This tutorial will guide you through the process of reviewing code for errors.": "Welcome to the Java Code Review Training System! This tutorial will guide you through the process of reviewing code for errors.",
    "In this system, you'll be presented with Java code snippets that contain intentional errors. Your task is to identify these errors and provide detailed feedback.": "In this system, you'll be presented with Java code snippets that contain intentional errors. Your task is to identify these errors and provide detailed feedback.",
    "Here's a sample Java code snippet with several errors:": "Here's a sample Java code snippet with several errors:",
    "This code contains several issues that need to be identified.": "This code contains several issues that need to be identified.",
    "First, let's see an example of a POOR quality review:": "First, let's see an example of a POOR quality review:",
    "Poor Quality Review": "Poor Quality Review",
    "This review is not helpful because:": "This review is not helpful because:",
    "It doesn't specify which issues exist": "It doesn't specify which issues exist",
    "It doesn't point to specific line numbers": "It doesn't point to specific line numbers",
    "It doesn't explain what's wrong and why": "It doesn't explain what's wrong and why",
    "It doesn't suggest how to fix the issues": "It doesn't suggest how to fix the issues",
    "Now, let's see an example of a GOOD quality review:": "Now, let's see an example of a GOOD quality review:",
    "Good Quality Review": "Good Quality Review",
    "This review is effective because:": "This review is effective because:",
    "It identifies specific line numbers": "It identifies specific line numbers",
    "It clearly explains what's wrong with each issue": "It clearly explains what's wrong with each issue",
    "It explains why each issue is problematic": "It explains why each issue is problematic",
    "It suggests how to fix each issue": "It suggests how to fix each issue",
    "Now it's your turn! Try writing a review for one of the errors in the code:": "Now it's your turn! Try writing a review for one of the errors in the code:",
    "Focus on this error": "Focus on this error",
    "Write your review comment for this error:": "Write your review comment for this error:",
    "Please write a more detailed review": "Please write a more detailed review",
    "Great job! Your review looks good.": "Great job! Your review looks good.",
    "Congratulations! You've completed the tutorial.": "Congratulations! You've completed the tutorial.",
    "Remember these key principles for good code reviews:": "Remember these key principles for good code reviews:",
    "Be specific about line numbers and issues": "Be specific about line numbers and issues",
    "Explain what's wrong and why": "Explain what's wrong and why",
    "Provide constructive suggestions": "Provide constructive suggestions",
    "Be thorough and check different types of errors": "Be thorough and check different types of errors",
    "Start Coding!": "Start Coding!",
    "Next": "Next",
    "Submit": "Submit", 

    "missingImportError":"Missing import statements for List and ArrayList",
    "offByOneError":"Off-by-one error in findUser loop (using <= instead of <)",
    "stringComparisonError":"String comparison using == instead of equals()",
    "nullCheckError1":"Missing null check before accessing userId parameter",
    "validationError":"No validation in addUser method",
    "nullCheckError2":"Missing null check before removing user",

    "codeIssuesHeader":"There are some issues in the code",
    "line1ImportError":"Line 1: Missing import statements for List and ArrayList. Import java.util.List and java.util.ArrayList.",
    "line10LoopError":"Line 10: The for loop uses <= which will cause an ArrayIndexOutOfBoundsException. It should use < instead.",
    "line12StringError":"Line 12: String comparison is done using == which compares references, not content. Use equals() method instead: if (user.getId().equals(userId))",
    "line9NullError":"Line 9: There is no null check before accessing userId parameter, which could cause NullPointerException. Add a null check.",
    "line6ValidationError":"Line 6: The addUser method doesn't validate the user parameter, which could allow invalid data. Add validation.",
    "line17RemoveError":"Line 17: No null check before removing user, which could cause NullPointerException if user is not found. Add a null check.",

    # Tutorial evaluation messages
    "Please improve your review: ": "Please improve your review: ",
    "Error evaluating your review. Please try again.": "Error evaluating your review. Please try again.",
    "Unable to evaluate your review. Please try again.": "Unable to evaluate your review. Please try again.",

    # Review format validation messages
    "review_cannot_be_empty": "Review cannot be empty",
    "please_use_format_line_description": "Please use the format 'Line X: description of problem' for each issue you identify.",
    "review_meaning_poor":"Your review needs more meaningful",
    "review_accuracy_poor": "Your review needs to be more accurate",
    "faile_review":"Please revise your review and try again. Focus on explaining specific line numbers, what's wrong, and why it's problematic.",

    # Tutorial related
    "tutorial": "Tutorial",
    "retake_tutorial": "🎓 Retake Tutorial",
    "tutorial_reset": "Tutorial reset! Starting tutorial...",
    "tutorial_completed_status": "Tutorial Completed",
    "tutorial_not_completed": "Tutorial Not Completed",
    "Evaluating your review with AI...": "Evaluating your review with AI...",
    
    # Error messages
    "Error checking tutorial status": "Error checking tutorial status",
    "Could not import AuthUI to mark tutorial completion": "Could not import AuthUI to mark tutorial completion",
    "Tutorial completed! You earned the Tutorial Master badge! 🎓": "Tutorial completed! You earned the Tutorial Master badge! 🎓",
    "Tutorial completed, but there was an issue saving your progress.": "Tutorial completed, but there was an issue saving your progress.",
    "logout": "Logout",
    "logout_success": "Successfully logged out!",
    "you": "You",
    "top_performers": "Top Performers",
    "view_full_leaderboard": "View Full Leaderboard",
    "users": "users",
    "of": "of",
    "no_badges_yet":"No Badges Yet"






}