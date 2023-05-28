class Band:
    """Represents a musical band, with members and methods for adding members and performing."""
    def __init__(self, name=""):
        """Initialize the Band with a given name and an empty list of members"""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of the Band, including its name and members."""
        return f"{self.name} ({self.members})"

    def __repr__(self):
        """Return a string representing the internal state of the Band."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band's members list."""
        self.members.append(musician)

    def play(self):
        """Simulate the band playing."""
        if not self.members:
            return f"{self.name} has no members!"
        band_playing = f"{self.name} is playing:"
        for musician in self.members:
            band_playing += f" {musician.play()}"
        return band_playing
