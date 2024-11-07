import os
import ffmpeg

class VideoConverter:
    def __init__(self, video_path):
        self.video_path = video_path

    def to_frames(self, output_path=None, fps=1):
        filename = os.path.splitext(os.path.basename(self.video_path))[0] #Obtiene el nombre del video
        frames_folder = os.path.join('outputs', 'video_to_frames_output', filename)
        os.makedirs(frames_folder, exist_ok=True)

        if output_path is None:
            output_path = os.path.join(frames_folder, 'frame_%d.jpg')
        
        (
            ffmpeg
            .input(self.video_path)
            .filter('fps', fps=fps)
            .output(output_path)
            .run(overwrite_output=True)
        )


    def convert_to_format(self, output_format=None, fps=None, video_codec=None, audio_codec=None, audio_channels=None): 
        filename = os.path.splitext(os.path.basename(self.video_path))[0]
        output_path = os.path.join('outputs', 'video_converted_output', f"{filename}.{output_format}")

        ffmpeg_command = ffmpeg.input(self.video_path).output(
            output_path, 
            **({'vcodec': video_codec} if video_codec else {}), 
            **({'acodec': audio_codec} if audio_codec else {}), 
            **({'ac': audio_channels} if audio_channels else {}), 
            **({'r': fps} if fps else {})
        )
        ffmpeg_command.run(overwrite_output=True)
