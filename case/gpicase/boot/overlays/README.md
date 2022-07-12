These are device tree objects are compiled from source using .dts files from
tsoliman and a post by kle4744 in the Raspberry Pi forums:

 - https://github.com/tsoliman/Retroflag-GPi-case
 - https://forums.raspberrypi.com/viewtopic.php?t=320939#p1922800
 
I am preferring to using these from source device tree objects so that it might 
be possible to change their behaviour, if required, in the future.

## KMS

Ludo use GLFW which required drm/kms. The dpi overlay for the GPi Case screen
is not compatible with KMS, so the GPi Case build of Retro Home falls back to
software (CPU) OpenGL rendering.

It might be possible to create a device tree KMS overylay for the GPi Case
screen:

 - https://forums.raspberrypi.com/viewtopic.php?t=322556
