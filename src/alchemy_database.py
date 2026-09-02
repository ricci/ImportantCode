def parse_f_strings_in_file(filepath):
    """Parse JSON strings that contain f-strings, converting them to regular values."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all occurrences of the pattern '{...' inside double quotes and remove surrounding context
        result_lines = []
        
        for line in content.split('\n'):
            if (line.startswith('{') or line.strip().startswith('}')):
                # Skip comments starting with //
                while '//' in line:
                    idx = line.find('//', 0, len(line)) - 1
                    comment_start = line[:idx] + '//'.ljust(256) if '/' not in comment_start else comment_start[1:]
                    
                    # Find the closing brace of this block (last '{' before '}')
                    open_braces_count = content.count('{', idx+3) - 1
                    
                    result_lines.append(line[:idx] + '}' + line[idx+len('//')+2:].strip())

        return '\n'.join(result_lines).replace('\r\n', '\n').rstrip()
        
    except Exception as e:
        print(f"Error parsing file {filepath}: {e}", file=sys.stderr)
