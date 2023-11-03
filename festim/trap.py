import festim as F


class Trap:
    """
    Representation of a trap

    Arguments:
        k_0 (float): pre-exponential factor of the trapping rate
        E_k (float): activation energy of the trapping rate
        p_0 (float): pre-exponential factor of the detrapping rate
        E_p (float): activation energy of the detrapping rate
        total_density (float): total density of the trap
        subdomain (Subdomain): subdomain where the trap is located
        name (str, optional): name of the trap
        mobile_species (Species, optional): mobile species trapped by the trap

    Attributes:
        k_0 (float): pre-exponential factor of the trapping rate
        E_k (float): activation energy of the trapping rate
        p_0 (float): pre-exponential factor of the detrapping rate
        E_p (float): activation energy of the detrapping rate
        total_density (float): total density of the trap
        subdomain (festim.Subdomain): subdomain where the trap is located
        name (str): name of the trap
        mobile_species (festim.Species): mobile species trapped by the trap
        trapped_species (festim.Species): trapped species
        empty_trap (festim.ImplicitSpecies): empty trap
        reaction (festim.Reaction): trapping reaction
    """

    def __init__(
        self,
        k_0,
        E_k,
        p_0,
        E_p,
        total_density,
        subdomain,
        name=None,
        mobile_species=None,
    ) -> None:
        self.k_0 = k_0
        self.E_k = E_k
        self.p_0 = p_0
        self.E_p = E_p
        self.total_density = total_density
        self.subdomain = subdomain
        self.name = name
        self.mobile_species = mobile_species

        self.trapped_species = F.Species(f"trapped_{self.name}", mobile=False)

        self.empty_trap = F.ImplicitSpecies(
            n=self.total_density,
            others=[self.trapped_species],
            name=f"empty_{self.name}",
        )
        if self.mobile_species is not None:
            self.make_reaction(self.mobile_species)

    def make_reaction(self, mobile_species):
        self.reaction = F.Reaction(
            k_0=self.k_0,
            E_k=self.E_k,
            p_0=self.p_0,
            E_p=self.E_p,
            reactant1=mobile_species,
            reactant2=self.empty_trap,
            product=self.trapped_species,
        )
