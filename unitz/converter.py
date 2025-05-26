from .units import UNITS, UNIT_ALIASES

class UnitConversionError(Exception):
    pass

def normalize_unit(unit):
    unit = unit.lower().strip()
    return UNIT_ALIASES.get(unit, unit)

def convert(value, from_unit, to_unit):
    from_u = normalize_unit(from_unit)
    to_u = normalize_unit(to_unit)

    if from_u not in UNITS or to_u not in UNITS:
        raise UnitConversionError(f"Unsupported unit: {from_unit} or {to_unit}")

    from_base = UNITS[from_u]
    to_base = UNITS[to_u]

    if from_base["category"] != to_base["category"]:
        raise UnitConversionError(f"Incompatible units: {from_unit} and {to_unit}")

    # Convert to base unit, then to target
    base_value = value * from_base["to_base"]
    return base_value / to_base["to_base"]
