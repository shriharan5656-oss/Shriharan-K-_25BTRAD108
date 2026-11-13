import csv, os

def run_payroll(inp="employees.csv", out="summary.csv", tax=0.12, pf=0.05):
    if not os.path.exists(inp): return print("File not found.")
    
    with open(inp, encoding='utf-8') as f: rows = list(csv.DictReader(f))
    processed, total = [], 0
    
    for r in rows:
        g = float(r['BasicSalary']) + float(r['Allowance'])
        d = g * (tax + pf)
        n = g - d
        total += n
        processed.append({**r, 'Gross': g, 'Deductions': d, 'NetSalary': n})
        print(f"{r['EmpID']} | {r['Name']} | Gross: ${g:.2f} | Net: ${n:.2f}")

    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=processed[0].keys())
        w.writeheader(); w.writerows(processed)
        
    print(f"TOTAL PAYOUT: ${total:,.2f}")

if __name__ == "__main__":
    with open("employees.csv", "w", newline='', encoding='utf-8') as f:
        csv.writer(f).writerows([["EmpID","Name","BasicSalary","Allowance"],["EMP001","John","45000","5000"],["EMP002","Jane","60000","8000"]])
    run_payroll()
