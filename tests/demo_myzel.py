"""
demo_myzel.py
Labor-Validierung des dezentralen Myzel-Protokolls (ISC-Immun) – DEBUG VERSION
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ISC_IMMUN import ISCImmunNode

def ausfuehren_labor_test():
    print("=" * 65)
    print("START LABOR-VALIDIERUNG: ISC-IMMUN MYZEL-PROTOKOLL (DEBUG)")
    print("=" * 65)

    # 1. Erstelle drei autarke Drohnen-Knoten
    drohne_alpha = ISCImmunNode("Drohne_Alpha")
    drohne_beta  = ISCImmunNode("Drohne_Beta")
    drohne_gamma = ISCImmunNode("Drohne_Gamma")

    # 2. Vernetze sie dezentral
    drohne_alpha.registriere_nachbar(drohne_beta)
    drohne_beta.registriere_nachbar(drohne_alpha)
    drohne_beta.registriere_nachbar(drohne_gamma)
    drohne_gamma.registriere_nachbar(drohne_beta)

    print("[Setup] Dezentrales Netzwerk etabliert: Alpha <-> Beta <-> Gamma")
    
    schad_signatur = "AST_MALICIOUS_X86_CONVERTER"

    # Debug: Ausgangszustand
    print(f"\n[DEBUG] Vor der Anomalie:")
    print(f"  Alpha blockierte: {drohne_alpha.blockierte_ast_signaturen}")
    print(f"  Beta blockierte:  {drohne_beta.blockierte_ast_signaturen}")
    print(f"  Gamma blockierte: {drohne_gamma.blockierte_ast_signaturen}")

    # 3. Simulation: Drohne Alpha entdeckt lokalen Angriff
    print("\n[Ereignis] Drohne_Alpha detektiert Schadcode-Struktur!")
    drohne_alpha.verarbeite_lokale_beobachtung("Infiltrierter_Sensor", ist_anomal=True, schad_signatur=schad_signatur)

    # 4. Debug: Nach der Anomalie
    print(f"\n[DEBUG] Nach der Anomalie:")
    print(f"  Alpha blockierte: {drohne_alpha.blockierte_ast_signaturen}")
    print(f"  Beta blockierte:  {drohne_beta.blockierte_ast_signaturen}")
    print(f"  Gamma blockierte: {drohne_gamma.blockierte_ast_signaturen}")

    # 5. Ergebnis
    print("\n" + "=" * 65)
    print("ERGEBNIS DER PRÄVENTIVEN IMMUNISIERUNG:")
    print("=" * 65)
    print(f"Drohne_Alpha blockiert: {schad_signatur in drohne_alpha.blockierte_ast_signaturen}")
    print(f"Drohne_Beta blockiert:  {schad_signatur in drohne_beta.blockierte_ast_signaturen}")
    print(f"Drohne_Gamma blockiert: {schad_signatur in drohne_gamma.blockierte_ast_signaturen}")

if __name__ == "__main__":
    ausfuehren_labor_test()