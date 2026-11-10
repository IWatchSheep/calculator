"""Electron Compton wavelength   [λ = h / (m c)]

Category : Physics > Physics
Formula  : λ = h / (m_e c)   (m_e = 9.1093837015e-31 kg, c = 299792458 m/s, h = 6.62607015e-34 J s; the wavelength itself, not the scattering shift)

Status   : ready to use - call compute(m=9.1093837015e-31, h=6.62607015e-34, c=299792458)
"""
NAME = 'Electron Compton wavelength'
SYMBOL = 'λ = h / (m c)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'λ = h / (m_e c)   (m_e = 9.1093837015e-31 kg, c = 299792458 m/s, h = 6.62607015e-34 J s; the wavelength itself, not the scattering shift)'


def compute(m=9.1093837015e-31, h=6.62607015e-34, c=299792458):
    """wavelength in metres"""
    return h / (m * c)
