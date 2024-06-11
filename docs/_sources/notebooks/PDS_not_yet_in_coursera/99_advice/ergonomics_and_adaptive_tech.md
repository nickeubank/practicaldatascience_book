# Ergonomics and Disability Accommodations for Programming

## Or: How To Not Hurt Yourself Doing Your Computer Job

*Note: None of these links are affiliate links. These are just recommendations I'm sharing from personal experience and lots of internet research I've done to accommodate my own medical issues.*

Most people come to data science (or other computer-based professions) when they're young and healthy. As a result, at the start of their careers, most data scientists don't think anything of hunching over a laptop for hours on end, banging away at their little keyboards.

As time goes on, however, almost everyone eventually realizes this is not a sustainable strategy. Even otherwise healthy people's wrists, backs, and necks will eventually start to object to this level of abuse. And that's assuming you don't have pre-existing medical issues to complicate your journey!

With that in mind, in this reading, I want to detail a series of tools you may find helpful in protecting your body and your ability to work, starting from simple interventions (an external keyboard and monitor) up through medium interventions (better desk chair, adjustable desk, monitor arm, ergonomic keyboards), and finally, tools that allow for people with more serious medical constraints — such as an inability to use a keyboard — to continue to work effectively.

## Simple Interventions

### External Monitor, Keyboard, and Mouse

If nothing else, I'm a *huge* advocate of anyone who works at their computer a lot getting an external monitor, keyboard, and mouse. They're relatively inexpensive and probably the most beneficial interventions available.

When looking at monitors, bear in mind you shouldn't spend more than $250 if you don't want to. Many monitors have really high resolutions, refresh rates, and color fidelity for gamers or professional photographers. But as of 2024, you can pretty easily get a 24" HD-resolution display for $150 and a 27" display for $200-250. Those aren't cutting-edge specs and may be a little less sharp than your laptop screen, but the real estate you gain more than compensates.

Keyboards and external mice, similarly, are a dime a dozen. And in combination, a monitor, keyboard, and mouse that allows you to sit up straight and look forward are probably the single most impactful changes you can make to your routine to protect your body.

Once you have these, make sure you use them correctly — if you search for "good ergonomics for computers," you'll find plenty of resources. The *top* of the monitor should be a couple inches below your eye level, the monitor should be roughly arm length from you, and your elbows should be about level with your keyboard. Just put a book under the monitor if it's too low and doesn't have its own arm.

### A Good Chair

A good chair can also be a really impactful intervention (depending on what you're starting with). Gaming chairs, for example, are often surprising inexpensive (compared to fancy office chairs that are priced for corporate buyers), are highly adjustable, and have high backs with good support.

### Don't Zone Out

It's easy when working at your computer to zone out and just work non-stop for extended periods. But taking quick breaks — spending a minute every 20 looking at something far away to let your eyes focus at a different distance, and/or standing and moving around every 20 minutes if you can — can be hugely beneficial.

To help you remember to follow these practices, consider a program that gives you little reminders to look away from your monitor or stand up occasionally like [Break Timer](https://breaktimer.app/) or [Time Out](https://apps.apple.com/us/app/time-out-break-reminders/). Fitness trackers like an Apple Watch or Fitbit can also remind you if you've been sitting for more than 20 minutes to move.

## Medium Interventions

OK, so you got the keyboard and monitor, and it doesn't feel like enough. What next?

Here are a few next steps, depending on what's causing you the most issues.

### Ergonomic Keyboards and Mice

If you are experiencing wrist pain or find yourself slumping forward because your shoulders are being pulled together and forwards by your hands both reaching to the keyboard in the middle of your desk, consider a split keyboard — they're *wonderful*. The easiest entry point for these is the [Kinesis Freestyle2](https://kinesis-ergo.com/keyboards/freestyle2-keyboard/) (I used it for years, about $100 for new ones, and refurbished ones for $55 in 2024). If you have money, they have some other models with clickier keys and other things people like, but in my experience, the gains are marginal compared to the jump from "regular keyboard to split keyboard." I *would* recommend the tent arms and wrist pads if you can get them.

The world of ergonomic keyboards goes keep, though, and there are other things you can get if you have the money. For example, some keyboards are curved so the distance from fingers to keys is the same everywhere, have keys where each finger gets a column of letters (ortho-linear keyboards) so they don't have to move side to side, and some keyboards have buttons for your thumbs (so you don't have to, say, stretch your pinky to reach the shift key). If your issues are back and neck-related, these may not be that helpful, but if your issues are wrist-related (e.g., RSI), this can reduce problematic finger movement a lot but take a little adjustment to the different key layouts. Examples include:

- [Kinesis Advantage 360](https://kinesis-ergo.com/shop/advantage360-signature/)
- [Glove 80](https://www.moergo.com/collections/glove80-keyboards/products/glove80-split-ergonomic-keyboard-revision-2)

Mice also come in many forms, including ones that are meant to be held [with your hand in a kind of vertical position](https://kinesis-ergo.com/products/#mice-and-pointing-devices), so you don't have to twist your wrist to set your palm flat on top.

### Standing Desks

Standing desks are amazing, not just because they let you stand, but they also let you make little adjustments when sitting to ensure things are always where your body needs them. Most people seem to like the [Uplift V2 Standing Desk](https://www.upliftdesk.com/uplift-v2-standing-desk-v2-or-v2-commercial/) (about $550). Wanna save a little money? Buy a [standing desk frame without a top](https://www.upliftdesk.com/uplift-v2-standing-desk-frame/) and buy a top at Home Depot. **Note:** if you're a person with significant medical issues, be aware putting together one of these is non-trivial! You'll want help.

### Monitor Arms

In the same vein, an adjustable monitor arm is the perfect partner for a standing desk — when standing at my desk, I put my monitor in a very different position from when I'm sitting, so having an easy-to-move monitor arm is really helpful. But if your monitor is on a stand that adjusts, the money-to-benefit ratio ([these are often like $200](https://www.amazon.com/Ergotron-Single-Monitor-Monitors-Up-Inches/dp/B01FW15TV6)) may not be great.

## Big Interventions: Fully Adaptive Tech

OK, now to the big stuff! Tools for people with more serious medical issues who struggle to use keyboards and mice.

### Programming With Your Voice

Voice dictation software is everywhere today ([most people use Dragon](https://www.nuance.com/dragon.html), but Google Docs has an in-built voice-to-text, too), but most of these tools are designed for people trying to dictate normal English speech (e.g., emails or letters). Unfortunately, these tools generally *don't* work for code — the syntax of programming languages is just too unlike everyday speech to be accommodated by these tools.

If you want a tool to help you *program*, there are a few options:

- [Talon Voice](https://talonvoice.com/). The website isn't super well documented, but **its free**, the community around it is **amazing**, and it's explicitly for programming. To get a feel for it, start by watching [this video on the tech](https://www.youtube.com/watch?v=YKuRkGkf5HU) and/or this [demo](https://www.youtube.com/watch?v=ddFI63dgpaI). I've used this off and on for years (depending on personal need), and I can attest that it's quite good.
  - Most people who use Talon start by cloning [these configurations](https://github.com/talonhub/community) into their ~/.talon folder. By default, Talon doesn't know any syntax — no alphabet, no commands for editors, etc. These configurations are a great starting place that most people fork, then tweak over time to meet their own needs.
- [Cursorless](https://www.youtube.com/watch?v=NcUJnmBqHTY) is another voice programming tool that uses Talon as its backend engine, but has some different syntax.
- The newest kid on the block is a tool for programming with [Github Copilot AI](https://www.youtube.com/watch?v=Bk7UdqoZUDk). This uses more natural language than the above, which could be a pro or con (it's less deterministic than Talon, like all Copilot behavior). No personal experience with this.

**Voice programming and Vim:** many people who voice program like vim or emacs, given they're explicitly designed for writing code without use of a mouse. With that said, if you don't use emacs or vim already you don't *need* those editors to be successful at voice programming. If getting started with voice programming feels daunting on its own, I'd recommend getting used to voice programming in your current editor before deciding whether transitioning to one of those editors is worthwhile.

### Using Your Eyes Instead of a Mouse

The [Tobii Eye Tracker](https://gaming.tobii.com/product/eye-tracker-5/) is a tool (originally for gaming) that you can use as a no-hands mouse replacement. You need one of their eye trackers, which you can then pair with [Talon](https://talonvoice.com/) to enable it to work as a mouse replacement. Talon also then allows for the use of your voice to induce clicks.

Again, the docs on the Talon site aren't great, but the community is amazing. Join the slack, ask for help, and look for youtube videos.
