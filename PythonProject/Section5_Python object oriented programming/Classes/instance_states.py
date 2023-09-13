class Camera:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording

    def record(self):
        if self.recording:
            print(f'{self.name} is already recording...')
            return
        print(f'{self.name} is recording...')
        self.recording = True

    def stop_record(self):
        if not self.recording:
            print(f'{self.name} is not recording...')
            return
        print(f'{self.name} is stopping to record...')
        self.recording = False

    def photograph(self):
        if self.recording:
            print(f'{self.name} can not photograph while record...')
            return

        print(f'{self.name} is photographing...')


c1 = Camera('Canon')
c2 = Camera('Sony')
# c1.record()
# print()
c1.record()
c1.record()
c1.photograph()
c1.stop_record()
c1.photograph()
print()
c2.stop_record()
c2.record()
c2.record()
c2.photograph()
c2.stop_record()
c2.photograph()
c2.record()
c2.stop_record()
# c2.record()
# print(c2.recording)
# print(c1.recording)
