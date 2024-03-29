def safe_convert(obj, new_type):
    if not type(new_type) == type:
        raise ValueError(f"Second argument must be a valid Python type")
    try:
        return new_type(obj)
    except ValueError:
        return None

def parse(file):
    if file == 'default':
        return {"type": "phoenix", "centerx": 0.2952345, 'centery': -0.254321, 'axislength': 0.6321, 'pixels': 640, 'iterations': 224}
    requiredFields = {'type', 'centerx', 'centery', 'axislength', 'pixels', 'iterations'}

    optionalFields = {'creal', 'cimag', 'parameter'}

    config = {}

    with open(file, 'r') as f:
        for lineNumber, line in enumerate(f):
            # Skip empty lines
            if not line.strip():
                continue
            elif line.startswith("#"):
                continue
            elif ':' not in line:
                raise RuntimeError(f"No ':' found in line {lineNumber + 1}")
            key, value = map(str.strip, line.lower().split(':'))

            # Check if the key is valid
            if key not in requiredFields and key not in optionalFields:
                raise RuntimeError(f"Invalid key '{key}' on line {lineNumber + 1}")

            # Add the key-value pair to the config dictionary
            config[key] = value

    # Check that all required fields are present
    missingFields = requiredFields - set(config.keys())
    if missingFields:
        raise RuntimeError(f"Missing fields: {', '.join(missingFields)}")

    # Check that the type is valid
    if config['type'] not in {'mandelbrot', 'phoenix', 'julia', 'burningshipjulia', "newton", "mandelbrot3", "mandelbrot4", "spider", "burningship"}:
        raise RuntimeError(f"Invalid type '{config['type']}'")

    # Check that the required fields are of the correct type
    try:
        config['centerx'] = safe_convert(config['centerx'], float)
        config['centery'] = safe_convert(config['centery'], float)
        config['axislength'] = safe_convert(config['axislength'], float)
        config['pixels'] = safe_convert(config['pixels'], int)
        config['iterations'] = safe_convert(config['iterations'], int)
    except ValueError as e:
        raise RuntimeError(str(e))


    if 'parameter' in config:
        try:
            complex(config['parameter'])
        except ValueError as e:
            raise RuntimeError(str(e))
    f.close()
    return config