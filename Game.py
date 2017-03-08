from Common import *

class Game:
    def __init__(self):
        # SCREEN_SIZEの画面を作成
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
        # 背景
        self.stage = Stage()
        # 自機
        self.player = Player()
        # 敵を管理
        self.enemy_manager = EnemyManager()
        # 自機の弾の管理
        self.player_bullet_manager = BulletManager()
        # 敵機の弾の管理
        self.enemy_bullet_manager = BulletManager()
        # アイテム
        #self.item = Item()
        # アイテム管理
        #self.item_manager = ItemManager()

    def update(self):
        self.stage.update()
        self.enemy_manager.update(self.player, self.enemy_bullet_manager)
        self.player.update(self.enemy_manager, self.player_bullet_manager, self.enemy_bullet_manager)
        self.player_bullet_manager.update(self.stage)
        self.enemy_bullet_manager.update(self.stage)

    def draw(self):
        self.screen.fill((0,0,0))   # 画面を青色で塗りつぶす
        self.stage.draw(self.screen, self.player)
        self.player.draw(self.screen, self.stage)
        self.enemy_manager.draw(self.screen, self.player, self.stage)
        self.player_bullet_manager.draw(self.screen, self.player, self.stage, (0, 0, 255))
        self.enemy_bullet_manager.draw(self.screen, self.player, self.stage, (255, 0, 0))
        pygame.draw.circle(self.screen, (255,0,0), (int(10), int(10)), 20) #アイテムの仮表示
        #self.item.draw(self.screen) どう引っ張ったら出てくるのかわからない
        pygame.display.update()  # 画面
