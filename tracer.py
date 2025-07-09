import sys
import inspect

def trace_lines(frame, event, arg):
    if event == 'line':
        local_vars = frame.f_locals
        vars_str = ", ".join(f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}" for k, v in local_vars.items())
        print(f"Line {frame.f_lineno}: {vars_str}")
    return trace_lines

def trace_script(script_path):
    print(f"--- Tracing {script_path} ---")
    
    sys.settrace(trace_lines)
    
    try:
        with open(script_path, 'r') as f:
            code = compile(f.read(), script_path, 'exec')
            exec(code, {})
    finally:
        sys.settrace(None)
        
    print(f"--- End of Trace ---")

if __name__ == "__main__":
    file = input()
    trace_script(file)
