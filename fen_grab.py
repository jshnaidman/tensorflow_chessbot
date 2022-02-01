from PIL import ImageGrab
from tensorflow_chessbot import ChessboardPredictor
import helper_image_loading
import chessboard_finder
import argparse
from helper_functions import shortenFEN, unflipFEN

temp_img_path = "C:\\tmp\\temp.png"

im = ImageGrab.grabclipboard()
im.save(temp_img_path,'PNG')

img = helper_image_loading.loadImageFromPath(temp_img_path)
tiles, corners = chessboard_finder.findGrayscaleTilesInImage(img)

predictor = ChessboardPredictor()
fen, tile_certainties = predictor.getPrediction(tiles)
predictor.close()
short_fen = shortenFEN(fen)
print("---\nPredicted FEN:\n%s %s - - 0 1" % (short_fen, active))