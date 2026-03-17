from decimal import Decimal, getcontext

# Set precision for oil & gas accounting
getcontext().prec = 10 

class AllocationEngine:
    def __init__(self, fiscal_total):
        self.fiscal_total = Decimal(str(fiscal_total))
        self.audit_log = []

    def calculate_pro_rata(self, well_data):
        """
        well_data: dict of {'Well_Name': theoretical_reading}
        """
        theoretical_total = sum(Decimal(str(v)) for v in well_data.values())
        
        # The 'Allocation Factor' is the most important part for the auditor
        allocation_factor = self.fiscal_total / theoretical_total
        
        results = {}
        for well, reading in well_data.items():
            allocated_vol = Decimal(str(reading)) * allocation_factor
            results[well] = round(allocated_vol, 4)
            
            # Log for the Audit Trail
            self.audit_log.append(f"Well: {well} | Factor: {allocation_factor} | Allocated: {allocated_vol}")
            
        return results

# FOR EXAMPLE
if __name__ == "__main__":
    # Total reading at the tank (Fiscal Meter)
    engine = AllocationEngine(fiscal_total=1000.00) 
    
    # Readings from the individual wells (Theoretical)
    well_readings = {"Well_001": 500, "Well_002": 300, "Well_003": 250}
    
    output = engine.calculate_pro_rata(well_readings)
    print("--- ALLOCATED RESULTS ---")
    print(output)
    print("\n--- AUDIT TRAIL ---")
    for log in engine.audit_log:
        print(log)
