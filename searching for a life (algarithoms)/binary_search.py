import time
import random

names = ['apple', 'banana', 'car', 'cat', 'dinosaur', 'dogs', 'elephant', 'fish', 'giraffe', 'horse', 'human', 'ice cream', 'jelly', 'jhon', 'kangaroo', 'lion', 'mandy', 'michael', 'monkey', 'noodles', 'orange', 'panda', 'quail', 'rabbit', 'snake', 'tiger', 'umbrella', 'violin', 'watermelon', 'xylophone', 'yak', 'zebra', 'zoo']
numbers = ['100', '102', '102', '104', '106', '108', '108', '109', '109', '111', '111', '112', '113', '116', '116', '116', '117', '117', '118', '119', '120', '121', '122', '122', '125', '125', '126', '128', '131', '135', '135', '136', '136', '137', '138', '139', '140', '143', '143', '143', '145', '146', '146', '147', '147', '147', '147', '149', '149', '150', '151', '152', '153', '153', '153', '154', '155', '156', '156', '158', '160', '160', '160', '161', '161', '162', '162', '164', '165', '167', '167', '168', '168', '169', '169', '170', '172', '174', '175', '176', '176', '177', '180', '181', '182', '182', '182', '183', '184', '187', '187', '188', '188', '189', '191', '191', '193', '195', '196', '196', '197', '197', '198', '198', '199', '200', '205', '205', '207', '211', '211', '212', '215', '216', '216', '216', '217', '218', '218', '219', '220', '221', '221', '222', '222', '222', '225', '225', '226', '227', '227', '228', '229', '230', '230', '231', '233', '234', '234', '235', '235', '237', '237', '237', '239', '239', '241', '242', '242', '243', '243', '245', '245', '246', '246', '246', '247', '248', '250', '250', '250', '251', '253', '255', '255', '256', '259', '259', '260', '260', '261', '261', '262', '263', '263', '264', '265', '266', '267', '267', '268', '270', '271', '272', '273', '273', '273', '273', '274', '275', '276', '278', '279', '281', '282', '285', '285', '286', '287', '287', '289', '291', '291', '292', '292', '292', '293', '293', '294', '297', '298', '299', '299', '299', '301', '301', '301', '302', '302', '302', '302', '303', '304', '305', '305', '307', '308', '308', '309', '311', '311', '313', '314', '315', '315', '315', '317', '317', '318', '319', '320', '322', '324', '324', '326', '327', '327', '327', '328', '329', '329', '330', '330', '330', '331', '333', '334', '335', '335', '336', '338', '339', '339', '342', '342', '342', '343', '343', '346', '347', '348', '349', '350', '352', '354', '356', '356', '356', '357', '359', '362', '365', '365', '367', '368', '369', '369', '370', '371', '371', '372', '375', '375', '376', '377', '381', '382', '383', '383', '383', '383', '383', '384', '385', '385', '385', '386', '388', '388', '388', '389', '389', '390', '395', '396', '396', '396', '396', '396', '397', '397', '397', '399', '399', '400', '400', '401', '402', '404', '407', '407', '408', '409', '409', '412', '416', '416', '419', '419', '420', '421', '422', '422', '423', '425', '427', '428', '428', '428', '429', '431', '431', '431', '432', '432', '433', '435', '435', '436', '437', '437', '438', '439', '440', '440', '442', '442', '443', '443', '445', '447', '448', '448', '448', '449', '449', '450', '451', '451', '452', '452', '453', '453', '454', '456', '457', '459', '460', '463', '463', '466', '467', '467', '470', '470', '470', '471', '472', '472', '475', '475', '475', '476', '477', '478', '480', '480', '483', '483', '484', '484', '486', '487', '489', '489', '489', '490', '490', '491', '491', '492', '492', '494', '497', '497', '497', '501', '503', '503', '505', '507', '507', '508', '509', '509', '510', '510', '512', '515', '515', '515', '516', '517', '517', '518', '519', '519', '520', '520', '520', '522', '522', '524', '525', '526', '527', '527', '527', '529', '529', '531', '532', '532', '533', '534', '534', '534', '536', '537', '538', '538', '539', '541', '542', '542', '544', '544', '544', '544', '544', '546', '546', '547', '549', '550', '551', '553', '556', '557', '557', '559', '562', '563', '563', '564', '565', '565', '568', '568', '569', '569', '572', '573', '573', '574', '574', '574', '575', '575', '576', '576', '578', '582', '582', '582', '583', '584', '585', '586', '589', '590', '591', '591', '591', '592', '592', '593', '593', '593', '594', '594', '595', '595', '596', '597', '598', '599', '600', '600', '601', '601', '601', '601', '602', '603', '605', '607', '608', '610', '610', '611', '612', '612', '612', '612', '612', '614', '614', '615', '617', '617', '618', '618', '621', '622', '622', '623', '624', '625', '627', '628', '631', '633', '634', '636', '636', '637', '638', '638', '639', '640', '640', '641', '642', '642', '643', '643', '643', '644', '644', '644', '648', '650', '650', '651', '651', '655', '656', '656', '656', '657', '659', '660', '660', '661', '662', '662', '668', '668', '669', '672', '672', '672', '674', '675', '675', '676', '676', '677', '678', '679', '681', '682', '682', '683', '684', '684', '684', '684', '684', '685', '685', '687', '689', '690', '691', '691', '692', '692', '692', '693', '693', '694', '694', '694', '698', '700', '701', '701', '701', '701', '704', '707', '708', '708', '709', '710', '710', '710', '711', '712', '712', '713', '713', '714', '714', '714', '715', '716', '716', '717', '717', '717', '718', '718', '719', '719', '719', '721', '721', '721', '722', '723', '724', '724', '724', '725', '725', '725', '726', '727', '727', '728', '729', '729', '729', '731', '731', '731', '733', '733', '734', '735', '735', '737', '737', '739', '739', '739', '742', '743', '749', '749', '750', '753', '753', '753', '754', '754', '754', '754', '755', '755', '757', '759', '760', '760', '761', '763', '763', '764', '765', '765', '767', '770', '770', '770', '770', '771', '774', '774', '776', '776', '776', '778', '779', '779', '779', '780', '781', '782', '784', '784', '784', '785', '785', '786', '787', '787', '787', '787', '789', '790', '790', '791', '792', '792', '793', '793', '793', '795', '795', '798', '799', '799', '799', '799', '799', '800', '801', '802', '803', '804', '805', '806', '808', '809', '809', '809', '810', '811', '811', '812', '812', '812', '812', '812', '813', '813', '814', '815', '815', '816', '817', '817', '820', '821', '822', '822', '822', '822', '826', '827', '830', '830', '831', '832', '833', '835', '836', '837', '838', '838', '840', '841', '841', '842', '843', '843', '844', '845', '847', '847', '849', '849', '850', '852', '853', '853', '854', '854', '855', '855', '858', '858', '859', '859', '860', '860', '861', '863', '865', '865', '866', '867', '867', '868', '868', '868', '869', '870', '870', '871', '872', '873', '873', '874', '877', '879', '880', '880', '881', '881', '881', '881', '883', '883', '883', '884', '885', '885', '890', '890', '890', '890', '890', '891', '891', '891', '896', '896', '898', '898', '899', '899', '900', '901', '901', '901', '902', '903', '906', '906', '909', '910', '910', '910', '910', '911', '911', '912', '912', '912', '913', '914', '914', '916', '916', '917', '919', '919', '920', '920', '921', '921', '921', '926', '926', '926', '927', '927', '931', '931', '932', '933', '934', '934', '938', '939', '941', '942', '944', '945', '946', '946', '946', '947', '948', '949', '949', '949', '950', '951', '951', '952', '952', '953', '954', '954', '956', '959', '961', '961', '963', '963', '965', '966', '967', '967', '967', '968', '969', '969', '971', '971', '972', '973', '975', '976', '976', '979', '980', '980', '980', '980', '982', '983', '984', '984', '986', '986', '987', '987', '988', '988', '996', '996', '997', '997', '998']


def binary_search(names, name):
    start = 0
    end = len(names) - 1
    while start <= end:
        mid = (start + end) // 2
        if names[mid] == name:
            return mid
        if names[mid] > name:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1


print(binary_search(numbers,str(random.randint(100,999))))

print(binary_search(names,"banana"))