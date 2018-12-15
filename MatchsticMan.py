import pygame
from pygame.locals import *
from sys import exit


# 玩家1类
class Hero(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = images_stand[0]
        self.rect = self.image.get_rect()
        self.rect.left += 80
        self.old_rect = self.rect
        self.frame = -1  # 帧数
        self.old_frame = -1
        self.last_time = 0
        self.direction = 0  # 方向
        self.speed = 2  # 行走速度
        self.attacks = pygame.sprite.Group()  # 攻击精灵组
        self.health = 100  # 血量

    # update方法控制精灵
    def update(self, key, current_time, rate=60):
        if key[K_w] or key[K_a] or key[K_s] or key[K_d] or key[K_f] or key[K_g]:
            # 攻击1
            if key[K_f]:
                attack_1 = Attack(self.direction, self.rect.center, 0)
                self.attacks.add(attack_1)

                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 3:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    if self.direction == 0:
                        self.image = images_attack_pose[self.frame]
                    elif self.direction == 1:
                        self.image = images_attack_pose_r[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect
            # 攻击2
            if key[K_g]:
                attack_2 = Attack(self.direction, self.rect.center, 1)
                self.attacks.add(attack_2)

                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 6:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    if self.direction == 0:
                        self.image = images_attack_pose_2[self.frame]
                    elif self.direction == 1:
                        self.image = images_attack_pose_r_2[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

            # 控制人物移动
            if key[K_w]:  # 上
                if current_time > self.last_time + rate:  # 根据时间判断是否进入下一帧
                    self.frame += 1
                    if self.frame > 5:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:  # 变换帧后改变图片
                    if self.direction == 0:  # 选择人物方向
                        self.image = images_walk[self.frame]
                    elif self.direction == 1:
                        self.image = images_walk_r[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

                self.rect.move_ip(0, -self.speed)  # 移动位置

            if key[K_a]:  # 左
                self.direction = 1  # 改变方向

                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 5:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    self.image = images_walk_r[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

                self.rect.move_ip(-self.speed, 0)

            if key[K_d]:  # 右
                self.direction = 0

                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 5:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    self.image = images_walk[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

                self.rect.move_ip(self.speed, 0)

            if key[K_s]:  # 下
                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 5:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    if self.direction == 0:
                        self.image = images_walk[self.frame]
                    elif self.direction == 1:
                        self.image = images_walk_r[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

                self.rect.move_ip(0, self.speed)

        else:
            self.image = images_stand[self.direction]  # 站立

        # 将精灵限定在屏幕中
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom < 220:
            self.rect.bottom = 220
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# 玩家2类，与玩家1类似
class Hero2(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = images_stand[1]
        self.rect = self.image.get_rect()
        self.rect.left += 400
        self.old_rect = self.rect
        self.frame = -1
        self.old_frame = -1
        self.last_time = 0
        self.direction = 1
        self.speed = 2
        self.attacks = pygame.sprite.Group()
        self.health = 100

    def update(self, key, current_time, rate=60):
        if key[K_UP] or key[K_LEFT] or key[K_DOWN] or key[K_RIGHT] or key[
                K_j] or key[K_k]:
            # 控制攻击
            if key[K_j]:
                attack_1 = Attack(self.direction, self.rect.center, 0)
                self.attacks.add(attack_1)

                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 3:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    if self.direction == 0:
                        self.image = images_attack_pose[self.frame]
                    elif self.direction == 1:
                        self.image = images_attack_pose_r[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

            if key[K_k]:
                attack_2 = Attack(self.direction, self.rect.center, 1)
                self.attacks.add(attack_2)

                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 6:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    if self.direction == 0:
                        self.image = images_attack_pose_2[self.frame]
                    elif self.direction == 1:
                        self.image = images_attack_pose_r_2[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

            # 控制人物移动
            if key[K_UP]:  # 上
                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 5:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    if self.direction == 0:
                        self.image = images_walk[self.frame]
                    elif self.direction == 1:
                        self.image = images_walk_r[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

                self.rect.move_ip(0, -self.speed)

            if key[K_LEFT]:  # 左
                self.direction = 1

                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 5:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    self.image = images_walk_r[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

                self.rect.move_ip(-self.speed, 0)

            if key[K_RIGHT]:  # 右
                self.direction = 0

                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 5:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    self.image = images_walk[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

                self.rect.move_ip(self.speed, 0)

            if key[K_DOWN]:  # 下
                if current_time > self.last_time + rate:
                    self.frame += 1
                    if self.frame > 5:
                        self.frame = 0
                    self.last_time = current_time

                if self.frame != self.old_frame:
                    if self.direction == 0:
                        self.image = images_walk[self.frame]
                    elif self.direction == 1:
                        self.image = images_walk_r[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = self.old_rect.midbottom
                    self.old_frame = self.frame
                    self.old_rect = self.rect

                self.rect.move_ip(0, self.speed)

        else:
            self.image = images_stand[self.direction]  # 站立

        # 限定在屏幕中
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom < 220:
            self.rect.bottom = 220
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# 攻击类
class Attack(pygame.sprite.Sprite):
    def __init__(self, direction, init_pos, mode):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        # 确定攻击特效位置
        if direction == 0:
            self.image = images_attack[int(mode)]
            self.rect = self.image.get_rect()
            self.rect.midleft = init_pos
        elif direction == 1:
            self.image = images_attack_r[int(mode)]
            self.rect = self.image.get_rect()
            self.rect.midright = init_pos

        self.frame = 0
        self.last_time = 0

    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > 3:
                self.kill()
            self.last_time = current_time


"""右跑APimg[10].png - APimg[14].png"""
# 窗口分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
# 背景素材
background_image = u'./images/man/bigBG[8].png'
game_over_image = u'./images/gameover.jpg'
hero_image_path = u'./images/man/APimg[].png'
hero_image_path_r = u'./images/man_r/APimg[].png'
attack_image_path = u'./images/man/AWepon[].png'
attack_image_path_r = u'./images/man_r/AWepon[].png'
# 画面帧率
FRAME_RATE = 60
# 画面周期
ANIMATE_CYCLE = 30

pygame.init()  # 游戏初始化
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)  # 创建窗口
pygame.display.set_caption('Angry MatchStick Man')  # 设置窗口标题
font_1 = pygame.font.Font(None, 60)
font_2 = pygame.font.Font(None, 30)
background = pygame.image.load(background_image).convert()  # 载入背景
game_over = pygame.image.load(game_over_image).convert()
clock = pygame.time.Clock()

# 载入图片资源
images_stand = []  # 站
tmp_img = hero_image_path[:19] + '2' + hero_image_path[19:]
images_stand.append(pygame.image.load(tmp_img).convert_alpha())
tmp_img = hero_image_path_r[:21] + '2' + hero_image_path_r[21:]
images_stand.append(pygame.image.load(tmp_img).convert_alpha())

images_walk = []  # 走
for i in range(4, 10):
    tmp_img = hero_image_path[:19] + str(i) + hero_image_path[19:]
    images_walk.append(pygame.image.load(tmp_img).convert_alpha())

images_walk_r = []  # 反向走
for i in range(4, 10):
    tmp_img = hero_image_path_r[:21] + str(i) + hero_image_path_r[21:]
    images_walk_r.append(pygame.image.load(tmp_img).convert_alpha())

images_attack = []  # 攻击
for i in ['252', '245', '248']:
    tmp_img = attack_image_path[:20] + i + attack_image_path[20:]
    images_attack.append(pygame.image.load(tmp_img).convert_alpha())

images_attack_r = []  # 反向攻击
for i in ['252', '245', '248']:
    tmp_img = attack_image_path_r[:22] + str(i) + attack_image_path_r[22:]
    images_attack_r.append(pygame.image.load(tmp_img).convert_alpha())

images_attack_pose = []  # 攻击姿势
for i in range(253, 257):
    tmp_img = hero_image_path[:19] + str(i) + hero_image_path[19:]
    images_attack_pose.append(pygame.image.load(tmp_img).convert_alpha())

images_attack_pose_r = []
for i in range(253, 257):
    tmp_img = hero_image_path_r[:21] + str(i) + hero_image_path_r[21:]
    images_attack_pose_r.append(pygame.image.load(tmp_img).convert_alpha())

images_attack_pose_2 = []
for i in range(19, 26):
    tmp_img = hero_image_path[:19] + str(i) + hero_image_path[19:]
    images_attack_pose_2.append(pygame.image.load(tmp_img).convert_alpha())

images_attack_pose_r_2 = []
for i in range(19, 26):
    tmp_img = hero_image_path_r[:21] + str(i) + hero_image_path_r[21:]
    images_attack_pose_r_2.append(pygame.image.load(tmp_img).convert_alpha())

# 创建玩家精灵
hero_1 = Hero(screen)
hero_2 = Hero2(screen)
group = pygame.sprite.Group()
group.add(hero_1)
group.add(hero_2)

# 窗口主循环
while True:
    clock.tick(FRAME_RATE)
    # 遍历事件队列
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))  # 绘制背景
    keys = pygame.key.get_pressed()  # 接收按键
    ticks = pygame.time.get_ticks()  # 获取时间

    # 更新精灵
    hero_1.update(keys, ticks)
    hero_2.update(keys, ticks)
    hero_1.attacks.update(ticks)
    hero_2.attacks.update(ticks)
    # 检测攻击精灵与玩家的碰撞，并改变血量
    if pygame.sprite.spritecollide(hero_2, hero_1.attacks, False):
        hero_2.health -= 0.5
        if hero_2.health == 0:
            break
    if pygame.sprite.spritecollide(hero_1, hero_2.attacks, False):
        hero_1.health -= 0.5
        if hero_1.health == 0:
            break
    # 绘制图像
    group.draw(screen)
    hero_1.attacks.draw(screen)
    hero_2.attacks.draw(screen)
    screen.blit(font_2.render("1", True, (182, 35, 38)), hero_1.rect.midbottom)
    screen.blit(font_2.render("2", True, (0, 0, 0)), hero_2.rect.midbottom)
    # 绘制血条
    screen.blit(font_2.render("Player 1", True, (182, 35, 38)), (0, 20))
    screen.blit(font_2.render("Player 2", True, (0, 0, 0)), (400, 20))
    pygame.draw.rect(screen, (50, 150, 50, 180),
                     Rect(0, 0, hero_1.health * 1.5, 20))
    pygame.draw.rect(screen, (100, 200, 100, 180), Rect(0, 0, 150, 20), 2)
    pygame.draw.rect(
        screen, (50, 150, 50, 180),
        Rect(SCREEN_WIDTH - hero_2.health * 1.5, 0, hero_2.health * 1.5, 20))
    pygame.draw.rect(screen, (100, 200, 100, 180),
                     Rect(SCREEN_WIDTH - 150, 0, 150, 20), 2)
    # 更新画面
    pygame.display.update()

# 游戏结束界面
while True:
    clock.tick(FRAME_RATE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(game_over, (0, 0))
    # 显示结束信息
    if hero_1.health == 0:
        over_text = font_1.render("Player 2 win!", True, (0, 0, 0))
    else:
        over_text = font_1.render("Player 1 win!", True, (0, 0, 0))
    screen.blit(over_text, (110, 240))
    pygame.display.update()
