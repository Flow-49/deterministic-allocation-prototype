# Hydrocarbon Allocation Engine Prototype
# Logic: Pro-rata Allocation with Uncertainty Propagation
from decimal import Decimal

def calculate_pro_rata(well_readings, total_fiscal_meter):
    """
    Calculates the allocated share of oil for each well based on their individual 
    meter readings vs the total fiscal (actual) tank reading.
    """
    theoretical_total = sum(well_readings.values())
    allocation_factor = Decimal(total_fiscal_meter) / Decimal(theoretical_total)
    
    allocated_results = {well: Decimal(reading) * allocation_factor 
                         for well, reading in well_readings.items()}
    
    # Audit Trace
    print(f"System Log: Theoretical Total: {theoretical_total}")
    print(f"System Log: Allocation Factor applied: {allocation_factor}")
    
    return allocated_results

# Example inputs for the interview
wells = {"Well_A": 450.5, "Well_B": 320.2, "Well_C": 229.3}
total_received = 995.0 # This is slightly less than the sum due to meter uncertainty

print(calculate_pro_rata(wells, total_received))
