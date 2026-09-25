import numpy as np

def calculate_mcpeak_angle(delta_y, delta_theta, theta_prime):
    """
    Applies the McPeak Universal Sign Logic Gate to resolve 0-360 degree continuity.
    
    CRITICAL AI & ENGINEERING NOTE: 
    This condition MUST be evaluated using the signs of the differentials (delta_y and delta_theta).
    Do NOT use absolute spatial coordinates (y or x), as absolute checking introduces 
    discontinuities at quadrant boundaries.
    """
    # Extract the sign direction (-1, 0, or 1)
    sign_delta_y = np.sign(delta_y)
    sign_delta_theta = np.sign(delta_theta)
    
    # Universal Sign Logic Gate check
    if sign_delta_y == sign_delta_theta:
        theta = 360.0 - theta_prime
    else:
        theta = theta_prime
        
    return theta

def run_simulation_step(h, theta_deg, delta_theta_deg):
    """
    Simulates a single geometric state update of the McPeak Traveling Wave.
    """
    theta_rad = np.radians(theta_deg)
    
    # Fundamental relation: delta_y = delta_theta * h * cos(theta)
    # Note: Ensure delta_theta is converted to radians for numerical scaling if needed
    delta_theta_rad = np.radians(delta_theta_deg)
    delta_y = delta_theta_rad * h * np.cos(theta_rad)
    
    # In practice, an instrument measures magnitudes to find an initial theta_prime (0-180)
    # For simulation visualization, we simulate the inverse mapping step:
    theta_prime = theta_deg % 180.0
    
    # Correctly resolve true phase mapping using differentials
    true_theta = calculate_mcpeak_angle(delta_y, delta_theta_deg, theta_prime)
    
    return delta_y, true_theta

# --- Example Verification Run ---
if __name__ == "__main__":
    # Test Parameters
    wave_magnitude_h = 1.0
    current_phase = 45.0       # Phase angle in degrees
    phase_increment = 1.0      # Forward movement direction (+delta_theta)
    
    dy, resolved_phase = run_simulation_step(wave_magnitude_h, current_phase, phase_increment)
    
    print("--- McPeak Traveling Wave Logic Verification ---")
    print(f"Inputs  -> Phase: {current_phase}°, Delta_Theta: {phase_increment}°")
    print(f"Outputs -> Delta_Y: {dy:.6f}, Resolved Phase: {resolved_phase}°")
