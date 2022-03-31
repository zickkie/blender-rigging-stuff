# Animation Space Switcher

**Space Switcher** is an add-on that gives you the control on **Armature Pose Bones** animation no matter what hierarchy they have.

With this add-on you can in fact swtich between **Local** and **Global** Space of the **Selected Pose Bones** by connecting the Bones to the **Empties** with the same Baked Transforms via Constraints.

## Add-on Functions:
_After being installed add-on's UI will appear at the N-panel within the Animation tab_

![layout](https://user-images.githubusercontent.com/59086089/146689174-cd5c648a-d244-4c60-9b36-eb8e62a66af8.png)

#### This add-on works with **Pose Bones** therefore major of buttons will be inactive unless you are in **Pose Mode**


#### ● 1. Animation

The name of the N-panel tab that contains the UI

#### ● 2. Bake Channels

Set of the animtion channels of Selected Pose Bones that you want to be "sticked" to created Empties

#### ● 3. Bake Frames -> From Scene

Set the desired Baking Frame Range directly from Scene settings (Scene Frame Start, Scene Frame End)

#### ● 4. Bake Frames -> Frame Start

Custom Frame Start

#### ● 5. Bake Frames -> Frame End

Custom Frame End

#### ● 6. Bake to Empties

Bake the selected animation channels onto created Empties (Selected Pose Bones animation itself won't be baked at this step)

#### ● 7. Attach Switch

Simple visual switch between Selected Pose Bones connected/not connected to the Empties

#### ● 8. Attach Clear

For the Selected Pose Bones delete everything (Empties and their Actions, Bones Constraints) that is connected to the last _Bake to Empties_ operation

#### ● 9. Clear Scene

Delete everything from scene (Empties and their Actions, Bones Constraints) that is connected to any _Bake to Empties_ operation

#### ● 10. Bake to Bones

Bake the final Empties animation back to the Selected Pose Bones (creates/overwrites Baked Action)

#### ● 11. Clear after Bake

Execute _Attach Clear_ operator after Bake

#### ● 12. To New Action

Create New Action after Baking instead of overwriting the existing


## Known Limitations:

1. When baking Scale, be awared that scale inherited with Share cannot be in any way represented by Transforms (as Transforms channels are stored separately).
That is why you may have a visual difference between "parented" Scale and Baked Scale in Animation.
2. Unfortunately classic Baking option in Blender doesn't provide with options to Bake only certain channels (e.g. only Loc, Rot or Scale). So if you need to tweak for example only Location it is a good idea to Bake everything to a new Action and then just copy-paste only those keys that are needed for your current Animation.

##

#### Update 31/03/2022:
As sometimes the default size of the created Empties can be far from what you find handy in terms of your current rig/scene you now can set the desired size of such Empties with the correspondive slider up to the "Bake to Empties" button:
![image](https://user-images.githubusercontent.com/59086089/160992640-e29c2d01-0016-4012-8602-2e5db2d4e700.png)
