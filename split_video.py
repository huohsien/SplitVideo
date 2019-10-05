import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Trim a Video at the given time hh:mm:ss')
    parser.add_argument('-i', dest='src', type=str,
                        help='Source video file to be trimmed.', required=True)
    parser.add_argument('-o', dest='dst', type=str,
                        help='Output trimmed video file.', required=True)
    parser.add_argument('-ss', dest='ss', type=str,
                        help='The begin time of the video to be outputed')
    parser.add_argument('-to', dest='to', type=str,
                        help='The begin time of the video to be outputed', required=True)
    args = parser.parse_args()
    if args.ss is None:
        args.ss = "0:0:0"
    cmd_str = "time ffmpeg -i \"{}\" -vcodec copy -acodec copy -ss {} -to {} \"{}\"" \
        .format(args.src, args.ss, args.to, args.dst)
    os.system(cmd_str)


if __name__ == "__main__":
    main()
