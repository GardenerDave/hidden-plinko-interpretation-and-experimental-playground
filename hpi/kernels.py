from dataclasses import dataclass
import math

@dataclass
class KernelConfig:
    kind: str            # "exp" | "powerlaw" | "osc"
    M: float             # tau_mem / tau_sys
    N: float = 0.0       # ell_mem / L_sys
    beta: float = None   # power-law index (0,1)
    omega: float = None  # oscillatory frequency

def K_exp(cfg: KernelConfig):
    tau = max(cfg.M, 1e-12)
    ell = max(cfg.N, 1e-12)
    def K(dx, dt):
        if dt < 0:
            return 0.0
        return math.exp(-dt / tau) * math.exp(-(dx*dx) / (2.0 * ell * ell))
    return K

def K_powerlaw(cfg: KernelConfig):
    assert cfg.beta is not None and 0 < cfg.beta < 1
    ell = max(cfg.N, 1e-12)
    def K(dx, dt):
        if dt <= 0:
            return 0.0
        return (dt ** (-(1.0 + cfg.beta))) * math.exp(-(dx*dx) / (2.0 * ell * ell))
    return K

def K_osc(cfg: KernelConfig):
    tau = max(cfg.M, 1e-12)
    ell = max(cfg.N, 1e-12)
    om = cfg.omega or 0.0
    def K(dx, dt):
        if dt < 0:
            return 0.0
        return math.exp(-dt / tau) * math.cos(om * dt) * math.exp(-(dx*dx) / (2.0 * ell * ell))
    return K

def make_kernel(cfg: KernelConfig):
    return {
        "exp": K_exp,
        "powerlaw": K_powerlaw,
        "osc": K_osc
    }[cfg.kind](cfg)
