import numpy as np

def get_steer_max(car_params, v_ego):
    """
    Calculate the appropriate steering limit based on vehicle speed.
    
    If the car_params include valid dynamic arrays (steerMaxBP and steerMaxV),
    use numpy interpolation. Otherwise, fall back to the static car_params.STEER_MAX.
    """
    try:
        bp = car_params.steerMaxBP
        v = car_params.steerMaxV
        # If dynamic arrays exist and have more than one element, interpolate.
        if bp is not None and v is not None and len(bp) > 1 and len(v) > 1:
            return float(np.interp(v_ego, bp, v))
    except AttributeError:
        pass

    # Fallback: if a static steering limit is defined, use it.
    if hasattr(car_params, 'STEER_MAX'):
        return car_params.STEER_MAX
    # Default if nothing is available.
    return 270
