# Used by:
# Implants named like: and 'Rogue' EM (6 of 6)
# Modules named like: Low Nozzle Joints (8 of 8)
# Implant: Genolution Core Augmentation CA-4
# Implant: Low-grade Nomad Alpha
# Implant: Low-grade Nomad Beta
# Implant: Low-grade Nomad Delta
# Implant: Low-grade Nomad Epsilon
# Implant: Low-grade Nomad Gamma
# Skill: Evasive Maneuvering
# Skill: Spaceship Command
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("agilityBonus") * level,
                           stackingPenalties = "skill" not in context and "implant" not in context)