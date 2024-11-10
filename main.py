def on_button_pressed_a():
    Player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if Bullet.get(LedSpriteProperty.Y) == 4:
        for index in range(4):
            Bullet.change(LedSpriteProperty.Y, -1)
            basic.pause(100)
        Bullet.set(LedSpriteProperty.Y, 4)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Bullet: game.LedSprite = None
Player: game.LedSprite = None
Speed = 800
Player = game.create_sprite(2, 4)
Enemy = game.create_sprite(randint(0, 4), 0)
Bullet = game.create_sprite(2, 4)
game.set_life(5)
game.set_score(0)

def on_forever():
    for index2 in range(4):
        Enemy.change(LedSpriteProperty.Y, 1)
        basic.pause(Speed)
    Enemy.set(LedSpriteProperty.X, randint(0, 4))
    Enemy.set(LedSpriteProperty.Y, 0)
basic.forever(on_forever)

def on_forever2():
    global Speed
    if Bullet.get(LedSpriteProperty.Y) == 4:
        Bullet.set(LedSpriteProperty.X, Player.get(LedSpriteProperty.X))
    if Bullet.is_touching(Enemy) and not (Bullet.get(LedSpriteProperty.Y) == 4):
        game.add_score(1)
        Speed += -30
        Enemy.set(LedSpriteProperty.X, randint(0, 4))
        Enemy.set(LedSpriteProperty.Y, 0)
    if Enemy.is_touching(Player):
        game.remove_life(1)
        Enemy.set(LedSpriteProperty.X, randint(0, 4))
        Enemy.set(LedSpriteProperty.Y, 0)
basic.forever(on_forever2)
