input.onButtonPressed(Button.A, function () {
    Player.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    if (Bullet.get(LedSpriteProperty.Y) == 4) {
        for (let index = 0; index < 4; index++) {
            Bullet.change(LedSpriteProperty.Y, -1)
            basic.pause(100)
        }
        Bullet.set(LedSpriteProperty.Y, 4)
    }
})
input.onButtonPressed(Button.B, function () {
    Player.change(LedSpriteProperty.X, 1)
})
let Bullet: game.LedSprite = null
let Player: game.LedSprite = null
let Speed = 800
Player = game.createSprite(2, 4)
let Enemy = game.createSprite(randint(0, 4), 0)
Bullet = game.createSprite(2, 4)
game.setLife(5)
game.setScore(0)
basic.forever(function () {
    for (let index = 0; index < 4; index++) {
        Enemy.change(LedSpriteProperty.Y, 1)
        basic.pause(Speed)
    }
    Enemy.set(LedSpriteProperty.X, randint(0, 4))
    Enemy.set(LedSpriteProperty.Y, 0)
})
basic.forever(function () {
    if (Bullet.get(LedSpriteProperty.Y) == 4) {
        Bullet.set(LedSpriteProperty.X, Player.get(LedSpriteProperty.X))
    }
    if (Bullet.isTouching(Enemy) && !(Bullet.get(LedSpriteProperty.Y) == 4)) {
        game.addScore(1)
        Speed += -30
        Enemy.set(LedSpriteProperty.X, randint(0, 4))
        Enemy.set(LedSpriteProperty.Y, 0)
    }
    if (Enemy.isTouching(Player)) {
        game.removeLife(1)
        Enemy.set(LedSpriteProperty.X, randint(0, 4))
        Enemy.set(LedSpriteProperty.Y, 0)
    }
})
