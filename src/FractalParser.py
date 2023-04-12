# def safe_convert(obj, new_type):
#     if not type(new_type) == type:
#         raise ValueError(f"Second argument must be a valid Python type")
#     try:
#         return new_type(obj)
#     except ValueError:
#         return None
#
def parse(file):
    if not file:
        return {}
    requiredFields = {'type', 'centerx', 'centery', 'axislength', 'pixels', 'iterations'}

    optionalFields = {'creal', 'cimag', 'parameter'}

    config = {}

    with open(file, 'r') as f:
        for line_number, line in enumerate(f):
            key, value = map(str.strip, line.lower().split(':'))

            # Check if the key is valid
            if key not in requiredFields and key not in optionalFields:
                raise RuntimeError(f"Invalid key '{key}' on line {line_number + 1}")

            # Add the key-value pair to the config dictionary
            config[key] = value

    # Check that all required fields are present
    missingFields = requiredFields - set(config.keys())
    if missingFields:
        raise RuntimeError(f"Missing fields: {', '.join(missingFields)}")

    # Check that the type is valid
    if config['type'] not in {'mandelbrot', 'phoenix', 'julia', 'burningshipjulia'}:
        raise RuntimeError(f"Invalid type '{config['type']}'")

    # Check that the required fields are of the correct type
    try:
        config['centerx'] = float(config['centerx'])
        config['centery'] = float(config['centery'])
        config['axislength'] = float(config['axislength'])
        config['pixels'] = int(config['pixels'])
        config['iterations'] = int(config['iterations'])
    except ValueError as e:
        raise RuntimeError(str(e))

    # Check that the optional fields are of the correct type, if present
    if 'creal' in config or 'cimag' in config:
        if config['type'] not in {'phoenix', 'julia', 'burningshipjulia'}:
            raise RuntimeError(f"creal and cimag are only valid for phoenix, julia, and burningshipjulia")

        try:
            config['creal'] = float(config['creal'])
            config['cimag'] = float(config['cimag'])
        except ValueError as e:
            raise RuntimeError(str(e))

    if 'parameter' in config:
        try:
            complex(config['parameter'])
        except ValueError as e:
            raise RuntimeError(str(e))

    return config