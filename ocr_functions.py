

def resize_img(self, img, factor = 1):
        return cv2.resize(img, None, fx = round(factor, 3), fy = round(factor, 3))
# ===========================================================================================

def resize_for_east_boxes(self, img):
    h, w = img.shape[:2] 
    # both RGB and grey images are handeled here
    return img[0:(int(h/32))*32, 0:(int(w/32))*32, : ] if len(img.shape) == 3 \
        else img[0:(int(h/32))*32, 0:(int(w/32))*32 ]

# ===========================================================================================
def cleaning(self, dirty_word, is_detection_result=False, check_english=False, remove_2letterNoise=False) -> str:

      # Cleaning stage_1: Removing all the characters except alphabets, apostrophie and spaces from the string
      whitelist = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ,'-/")
      dirty_word = ''.join(filter(whitelist.__contains__, dirty_word)).strip()

      # Cleaning stage_2: Removing non-meaningful words
      if is_detection_result and check_english:
          words = set(nltk.corpus.words.words())
          dirty_word = " ".join(w for w in nltk.wordpunct_tokenize(dirty_word) \
                  if w.lower() in words or not w.isalpha())

      # Cleaning stage_3: Removing upto 2 letters (noise) from the start and end of the OCR detection result
      if remove_2letterNoise:
          dirty_word = dirty_word.split(" ")
          direction = 1

          for i in range(2):
              for j in range(len(dirty_word)):
                  if len(dirty_word[direction * i]) < 3:
                      dirty_word.remove(dirty_word[direction * i])
                  else:
                      break
              direction = -1

      clean_word = (' '.join(dirty_word))

      return clean_word
 # ===========================================================================================
def img_crop(img, complete_width=False):

    h, w = img.shape[:2]
    if not complete_width:
        start, end = w/13, w/1.3
    else:   # crop for the complete card width
        start, end = w/18, w/1.3
    
    # tweak these values to get good result for title croped image
    start_row, end_row = math.floor(h/28), math.floor(h/9)  
    start_col, end_col = math.floor(start), math.floor(end)

    return img[start_row:end_row, start_col:end_col]
  
 # ===========================================================================================

def grey_val_ratio(img):
    max_grey, min_grey = img.max(), img.min()   # getting max and min grey values
    
    max_grey_count = np.count_nonzero(img >= max_grey*0.70)
    min_grey_count = np.count_nonzero(img <= min_grey*1.30)
    r_white = max_grey_count / img.size
    r_black = min_grey_count / img.size

    print(r_white, r_black)

    return r_white, r_black, max_grey, min_grey
  
 # ===========================================================================================
  
  def dev_similarity(name, detection):     # it will compare detection result with the card name. 
    return SequenceMatcher(None, name.upper(), detection.upper()).ratio()
 # ===========================================================================================
  
  def enhance_contrast(img, show_img=False):
    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l_channel, a, b = cv2.split(lab)

    # Applying CLAHE to L-channel
    # feel free to try different values for the limit and grid size:
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l_channel)

    # merge the CLAHE enhanced L-channel with the a and b channel
    limg = cv2.merge((cl,a,b))

    # Converting image from LAB Color model to BGR color spcae
    enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    if show_img:
        cv2.imshow("Enhanced Contrast", enhanced_img)
        cv2.waitKey()

    return enhanced_img
  
 # ===========================================================================================
def size_threshold(bw, minimum, maximum):
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(bw)
    for val in np.where((stats[:, 4] < minimum) + (stats[:, 4] > maximum))[0]:
      labels[labels==val] = 0
    return (labels > 0).astype(np.uint8) * 255

def y_centroid_threshold(bw, minimum, maximum):
    # this function finds the centroid of each patch and only keeps those whose points are between (min, max) range
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(bw)
    for val in np.where((centroids[:, 1] < minimum) + (centroids[:, 1] > maximum))[0]:
      labels[labels==val] = 0
    return (labels > 0).astype(np.uint8) * 255


def noise_reduction(img):
    h, w = img.shape[:2] 
    min, max = int((h/2)*0.6), int((h/2)*1.6)
    clear_img = y_centroid_threshold(img, min, max)
    return clear_img

 # ===========================================================================================
  
 # ===========================================================================================
  
 # ===========================================================================================
  
  
  
  
  
  
