"The Command Pattern Use Case Example. A smart light Switch"
from light import Light
from switch import Switch
from switch_on_command import SwitchOnCommand
from switch_off_command import SwitchOffCommand

# Create a receiver
light = Light()

# Create Commands
switch_on = SwitchOnCommand(light)
switch_off = SwitchOffCommand(light)

# Register the commands with the invoker
switch = Switch()
switch.register("ON", switch_on)
switch.register("OFF", switch_off)

# Execute the commands that are registered on the Invoker
switch.execute("ON")
switch.execute("OFF")
switch.execute("ON")
switch.execute("OFF")

# show history
switch.show_history()

# replay last two executed commands
switch.replay_last(3)

# ***********************
# switch: "The Invoker Class."
# Light(): the receiver class
