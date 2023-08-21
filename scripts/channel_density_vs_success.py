import subprocess
import sys
import json
import time

invoices = ['lntb1m1pjdcqvqpp53yc5y9q6ze3nfkrtz7lnff8m4ewklvz9thlr7ts0lmzastknhd0sdqqcqzzsxq9z0rgqsp5a57pzydt3lyzu4v7l825vv6g9seed6vg9gu7vqe6f5cylu4excxs9q8pqqqssqrx2770gzcnd9vdeer8luuu55mxfrhzq5zq2rghf26p5z9wpuy8hq6pwzm78hq33ktk7dfgl8ye2dj23qrvtehqdugg536x2tjq6hshgpa4wmk4', 'lntb1m1pjdcqvqpp59qem9emlp9w2qyufxnqu02e288zrdvryu808nx4htscrtghusslsdqqcqzzsxq9z0rgqsp5gq4n2j5prer2p6qc3c4cmjj5d2qyfakg5fl6ncp3ckvlfy6mxa3s9q8pqqqssqnlf26c7c9c7xk7plv9u9f04ql0dee3x24npvu8uvdn97akkz5zgh73kx8mm22cz2pnnuflj5duqcfhmytqga98jvqfs7mj3jp7jmm7gqygetdk', 'lntb1m1pjdcqvqpp5xpqsmm90tceayk7umkj8f75tlg3ns2m8yv4dcumxwpsd4g8j7gtsdqqcqzzsxq9z0rgqsp5vp3jzdcad5cgef5al3a7nnr9ntgntlqar6uksrdhw4j7l6uzt09q9q8pqqqssq7dwyfh2jpcmh77rd6e800c7y2x5etudm4jjyl2z9j0yznzetxhshatqhpqd5c09y2d6evm9mudpdk8kjfe3zlrhhp8wzkxky2zzqnvqqdnqhjm', 'lntb1m1pjdcqvqpp5ut8tz2gnalkrez2js0x2fuccq54a69yjq8ha6a3nu3pv57wsfaqqdqqcqzzsxq9z0rgqsp52na0an4772xugntg9jtjw05lqqm59hy0yfhuj9a623pxtje9jtcs9q8pqqqssq24pank66gspzlzlkm90r8acy4a97t6le6jyl0wwac4cfw6j22x5929sckxenrkgx8ntt77ejtq2vd9c2rmxcxj7yws6jhlhdj6z6ecgq63ftdx', 'lntb1m1pjdcqvqpp52uau3rzgj8mrh9y3j2d4n3jecm72g3nyl538s59whgnp4h8g0j9qdqqcqzzsxq9z0rgqsp5rrdhsjpz0cmlyafnu9ghz3e8t6mwrshdsdtw4ur2qg6mmrkpjkfq9q8pqqqssqdef5cyacqlhhfuzvky8565zyrl4x6sca4hl4gqljg56wqd0kekdhru9w37pppmwwvfpyzr7ql3tj0h64w7v0aex8huufrwuys202cacp69lvt2', 'lntb1m1pjdcqvqpp5ftk9vv2yvhyuk89da036avx6jatmtm5xr42fduym2adjqy8hl55qdqqcqzzsxq9z0rgqsp57cw4gdr527tmu2q6kuu68srzsv3zqffanrtgnj7s0qmufkn9569s9q8pqqqssq2zawtvrrqyuvtek7srzwvr0vr2wpmffwgdrxu6xkrppddh39vkrh26yhczhj4x833l27wy22cnygc9wvxddn28sld97ymex5w3fkumgqrreqgm', 'lntb1m1pjdcqvqpp5uxd8j67jcy5gsem59tvdk9feuj89mz29v9a0e6h85axdah2y24xqdqqcqzzsxq9z0rgqsp5pejmkq57tpjhpw597044kaqdrr5lpmmcjtez55n2nut68lqsmlxq9q8pqqqssqlakd9avhcwdmmkr505sr8g5320wg8qqsxswj6evqgnjxasku2nz9ltknu39en8hns2vzc45l9axs6p67lzswhpvfkhyrshzeh4a55fsqx4ych2', 'lntb1m1pjdcqvppp5ad7dvn7dxach435yzqtldxmdplh0j2uuzx4e6l2ahkwengzpja8qdqqcqzzsxq9z0rgqsp5mgy2q8n5gp7tzw4udf43x4s0ps896wcsz093nwcrp07t4yws5d0q9q8pqqqssqe3twztktwyg8ak6ygfkz49racdd3jlhwyjahw2p8ss8ct3mthlm9c3x5kd3r85w5wfndkhr8vku8g65qvrahwxx853w8n2hj9efj6wcqdmd48y', 'lntb1m1pjdcqvppp5hv7a0m4w7d3z9ch7hrrt2g5zq9xn7hfj2ujvc57l4q4qaqn4wxaqdqqcqzzsxq9z0rgqsp5lx69666m45tcdrlxslra9qy4djmgtw7a0ju0rh2xqwyknn0ww9yq9q8pqqqssqa9a4lh96d83zzqpcexz24q8g4sh2wceqdav0hwgl6pq0m8tzqnm4ml409guv4ag5hfmfquq5dvh5h30t6kaa7kzfaaff98z7vyxlwlcpd4c7cq', 'lntb1m1pjdcqvppp58k27uvcqyeuy766vf3zdxad9jv9flzw7v0apguntjw3e3dmfpkpsdqqcqzzsxq9z0rgqsp5x422axvjr0sle3py9rzj39vltsg7sjfzqzk5twes826m08chh7cs9q8pqqqssqz6g6hf3370ypv2xvehxwjcxrmrqzjac6ayrz07m4f9ztqeu0nhdstlqlz26mulualdg90xt4kzjs9wfvem7lw2qf87tdk6ysvdwxqvgqhtc6p5', 'lntb1m1pjdcqvppp58e7rpf0u6q3fvz0lz4eg3kcew80490ev0vn9xn023yxp5n2xsrjqdqqcqzzsxq9z0rgqsp5kw6xfql8gxq30d4t5prpu02s7uvj8a6ct8ad5laarf7w2q24vwrs9q8pqqqssqj6e8cf8ulf4gwykd2xpvvmwwzaxxk93drcq7lqdtjndpalu6xenpphr604l7cd6gke58lpvwa4x5csfq8eh6kl4yctxs3zmdgeztz2cptk523c', 'lntb1m1pjdcqvppp5nt97j9khpmcn5vz6c4ejdehtj9dhrrda8unnv5m00jawg3yfkj9qdqqcqzzsxq9z0rgqsp53ke6r8aldnd0pxt855yl9ww07wzw6yhgpeagngtct5ckgp2mg5ms9q8pqqqssqtel4agfuc5c5pmjy5zx8985qhlaa3gx27ns4ue6qww666mhljxyqfr2j33jgp66plk88uqd2fansg7sntxvrrzvks6l4asty30l325spsvduy4', 'lntb1m1pjdcqvppp57jt6gqts4kz2j99mlpdxad2gpwjdw3sw70vj44n4lqm47mu5pu2qdqqcqzzsxq9z0rgqsp56gze42zp4tsdvqeyerukecrlm3nh9rfz0caseaq6s995uafwdkuq9q8pqqqssqux2rjvxj6y8h0hce4sq68xrf5ymg7rwfulhjqc0rkt7q8ql8xplsgmahlcm92g9pdx8yvj9r8pn59xdzhw3w3r8gkrspmndp5jjplwgpf62ruz', 'lntb1m1pjdcqvppp527stje6rkhymc0vms8pqhfpzeu9rzrrxq77m26d980h2qff5t59sdqqcqzzsxq9z0rgqsp59h2wcz6huavcgw5l8rxazfzmjxn3f7q4uy7t6s035cfvcfae3gfq9q8pqqqssq56kz5a3wp43f0stk9grpzg4kf72dwdprsmee7szps5fhe220ljg437jhmlal6304d08v98vc85h0pqm6a43jz3kqx9sgvstsejrcjhqp5fjcyf', 'lntb1m1pjdcqvppp5tgqxmhnj7r3n9cls86n2qz4ney2c226lvc3lt609nh5ufw9wqkhqdqqcqzzsxq9z0rgqsp5whc757u5792ur0p8fqe3sgu50rwfekgd2gw4hc6jl3083p9fgm9q9q8pqqqssqdztpczyetjwx584kypylcylz9fv653vctseuvtmh6qy4qra33x9qwx5wk29kr48mpdz8qul5s6yj7evhu08xrwx99zmcjxnefjysjhcpdmp8yt', 'lntb1m1pjdcqvppp5kurwwrx8gner6w499alpj0yprqa7ej0vumr2rvg772nv4jpwfvwqdqqcqzzsxq9z0rgqsp5a85jjusgf08qm6aqe74tvpa5vgfqz6daxe4e80hgknalxjxw6jpq9q8pqqqssqtq6sudcpjvens5epl7wdraa3gka3upx528hfpxcchpwl0y08wghxkqcpwen4yw7vlsmsaknqw73phasvm0fks4vkta0t2kquvqzs02spzk72g2', 'lntb1m1pjdcqvppp50862aulshqke50elv0hceagdhyt6lumvvgl2c3p60tqruy8t34msdqqcqzzsxq9z0rgqsp5tz2c4su7atnqmcufftlz0m72jnve08qvq202a627u4d5n3dv6k0q9q8pqqqssq57vrkjuda4ej5dprzxqxum9ggcz72ucgksd8t94rzrmppgs83qf983tqwn3unfta7s6wz0krfhfanwmtrphmtgdwc50s4y46esexveqqmsyppu', 'lntb1m1pjdcqvppp5hke5j90xf7nx9qp2jsnsr3zq68fllrvftf5lqatu5kjmpwasxvwqdqqcqzzsxq9z0rgqsp5c990qwawkkvcmaq9m9y0cx4p2xwt3tse2m97kqhakd9evsvslafq9q8pqqqssq4au7zx5lz6awjvqw3ne843k9c2kge36ckdfwhk5tj96cpm3f77g5zq58lgtzsyvsthd3jmspqunn7adw8jw8g73vvrvmcqvrm0mt9pgpk4cjmm', 'lntb1m1pjdcqvppp555xxqdvprq7a6jx7ydfrpdypppt76t9xq0ydttcsh02wffgctaqqdqqcqzzsxq9z0rgqsp5whfpllamg4dsthsxejj6mavxtjkq4u6ywgk7gee0y78v0akcc27s9q8pqqqssqx9kl66ednnudcwlf5wmnmc36qqq0kqj8h3hn3pknv2h7qgnslmvrakpt2a8svmf5pp94jlkr998m0tzyxps6lgwpu4f8t5rf4jhahtgpcu4pkv', 'lntb1m1pjdcqvppp520g7repee0durzntg8m6p2t5rr4n3fxck8xvqrkqjcve5l8yyrkqdqqcqzzsxq9z0rgqsp530kxhrdf8g3jgh9qcut6g0uj45p6zyekllaeufy8zqgukl0laxas9q8pqqqssqcdm9p8kuwzl82xqdacmvelp6k0gkpfmuquhpnqqvza8l8jp2camj2a3ad8zycmlmsxhnw2k3csawj0lmmap7atx608up6yh9g00497sqq97guv', 'lntb1m1pjdcqvppp5dl6mnjz33wwzhuuulcas2q70h0knjxfw87yhfjxflzrd6c6ew5sqdqqcqzzsxq9z0rgqsp5grp8h6exefjrzy0myuruqxruutyvxr9p226g7c9h4mk7r9rhqaeq9q8pqqqssqkd3w7nadcevtgr406a34xquu8jtnt5465danefydnw5tt43xpje5j2jg6a2l7jldzq59adllnw7uxsce8pe6s7gc7ceqd8qggmc78jqqn9k37n', 'lntb1m1pjdcqvppp5m8wy8upx7yhpkxdcvqkddqfh4ppt6fj9v3xwtaeand9797yqtpqqdqqcqzzsxq9z0rgqsp58jl20n4u5392xlkhujss8tc2sed9ykpxrf28n0ud2vjl5w6wx47q9q8pqqqssqqck63psl37dlq9ncn625780gpufyeujd7n50zxlh7clx4j7wtdsjpetqzhwthw2e6fte8z8x7uvr2ccnxdjq99jdpazck5xh9wh5ljgpwd6dq0', 'lntb1m1pjdcqvppp5s5qqpsa6gawxkqwdyrrffvh53cdj3n3enp8wua7l45kv998jurrqdqqcqzzsxq9z0rgqsp5kflhflpuyj4x9s9srrjcpk24kmhhyaxf7xk4a8vg8993c08lrawq9q8pqqqssqhz4m7sfcy7j7u3atxgxltx76lfapmjyulgj2drms3z0rznp78zl8wtvjj444k8rjythvt9r6aljezgvh48cxcqaduxndrv93hljn05sp2jmvnd', 'lntb1m1pjdcqvppp58qgkgfstq0krnv25lck5gkz2d32jgdsp2exvfd4duvx8ehxvjgyqdqqcqzzsxq9z0rgqsp5qgfdd79e3hnwrz7n59cgre4ccy7wp8l38aqx56tq4w8m4cg52prs9q8pqqqssqprmlgvqsk63s5s8nmvtkxnsmzw7gzzvkrd832tuz395429fj37l9vjnjzpddq4t657ulf6r9auf297tsls6cv2alyky2rxq96032pucq4wcn35', 'lntb1m1pjdcqvppp5fztwjl5ea2xn5tj55xnp5wyqc84495qucw8kz9dlgkd9lnrfe2zsdqqcqzzsxq9z0rgqsp5ke8m6t8y89jer9hwrptwfw6tpnmkzhsdzydse2razw4g5gdjtw4s9q8pqqqssqwea2kqmsx97qw2m5eg4fkawmwzgp9gf2jarjmtpuxdehdkqhsuwj6tvuz3xkfnsstgchx6pndzzkajjv99rq5p9fxqdwa2jr3x2tsfsq4lwvf4', 'lntb1m1pjdcqvppp5ztjw7sj4u56jnrpashtjajy2zcdf5gath5gd7vz60sxu8p64g86qdqqcqzzsxq9z0rgqsp5zjx32a920c5zw5nwr7leqpfqqg265d5vuprdprh0736jc87h3cuq9q8pqqqssqm4htt3xkn8ngeumhxf722489jdly3wycxz8dw8vd6h20yn79t6cka45stlfgsr8mdl6cdp0rq0h58ws5xupxvfqreey465lm8sxmytqq7thluw', 'lntb1m1pjdcqvzpp5h5kv86wwppvhyplz3fnm542kadcflgw3r226yw8j594kr85lg82sdqqcqzzsxq9z0rgqsp57vm83la52m9e8xwts45n2py74v36ely9tdqes9r0lffdwwg5pxhq9q8pqqqssq7zxudp54j60pq326s47cjgguuq37har0qqa64zlcl8gh27uwsl6qux7y7n2yctc57w5t8q08qf5ps3j9966ycn70k38nnyl8f23d68qpj8skty', 'lntb1m1pjdcqvzpp5uv0vpn4a43dr0fjd0a5ze0esl0yyg4463hfyayxrvtgxjfkn5adqdqqcqzzsxq9z0rgqsp52q0rzrrvv4y80ffs9vp6vlxccqsfy3654wz03pjh3h570c4w4p5s9q8pqqqssq5r7vnz4e9z6epsf9x5fu66syu3nw9c2prks9yrw7evg9t0evugn99djjlcmztedvy90jxesytkrwepn4mkg969q8thmva9plstytk6gq3f5jt9', 'lntb1m1pjdcqvzpp5ewcjt2fvd0vq3s969ehzn8earplp6adrcacuy2yds0ful4zdc9rqdqqcqzzsxq9z0rgqsp5rsuqhl0uhnysfzy0aw5ex9cvdaz939gxgfpy2xp2jplehp62fuqq9q8pqqqssq7qnm2q3xqxuv6lacajqcu6us2wdxfduegjjn2kfzfj65l3dne68r7te9rqqrtytajgeny5asgc9l4cjg8d8ssp3psgcsvqn8zevrsyqpq7dr6w', 'lntb1m1pjdcqvzpp52frz8r2qukqe27m2g80f5f5gryrp7jf505t4mrnmgwtqjs50nrqqdqqcqzzsxq9z0rgqsp5sqhhxtcjyqfauedplj4vfjqwujcl5htxgw27a8y7prjreyf5kl4q9q8pqqqssqxd6ugxtl2t7ecd5y98nes9lmaqtcyjmyg6aka4c9fy3d2htcas8zeat7p96h9vtcgcehdlhxy5fn0ur4gqxnchlgue9m79cezgmledspw2w6ww', 'lntb1m1pjdcqvzpp5sushcam99qzq2y6y9769alexp6rg6fjgsvfv2ujj4fh6elnqtazsdqqcqzzsxq9z0rgqsp5aedm4408mdmg6auqnvpa4k0ekl4ex3xw3j32583gf8nxam377xuq9q8pqqqssq7gz3t4l29g2dux5dhgmanwumq9ct0swmum3jsedghwa7ajcep8z4phxjda44ymz58cprx32k0a4md3sz8xmzmw7mu83nffvuawyax2qp3ndpdr', 'lntb1m1pjdcqvzpp59lazkrgw00c725pq9ju8cz8hnhwepm0dgvpcxna40fzlv0wxg2ksdqqcqzzsxq9z0rgqsp5d82zt7tj623y8xvfvxk3wdl5zgrmsn2a0k23785g72d8duzqc0rs9q8pqqqssqx4un0hhsjv7yfdsdwg6c86ndq24a6dtm8ac4xlrertvk8s2psxzpy8axr34f3qddq8jmu9yafvquu9rz4xlva8ut3d2k5uvnfvg46pgplzue5p', 'lntb1m1pjdcqvzpp57x6mxsp64agqmd00w02a7udn9van2h7x2kqmjjmqgjp4jz46hhesdqqcqzzsxq9z0rgqsp5a0wdt68n7uf6geqzeu9j04rxph83fmcp9h0pmdmtlprt6xl8geaq9q8pqqqssq4rw6m9purmrzykpxxgud682j0ljzvskwxjh8x5al79h9laj4pskyyrna589w70n66df0t7aczaplqx3y95pn26wdn06w04fyffv83sqqepjvrn', 'lntb1m1pjdcqvzpp5wms3t3zggtqugf249867memjt5h2cy2rcyem334ukq2n078tq3wsdqqcqzzsxq9z0rgqsp5nuthty4gcg2r5s7xayh9gzxg83rqy9cdedujhcls2uq2nvc84fls9q8pqqqssqc777wdy8wkv4dy9uyw4xfjsr4zgekmksn9v0d7pq0h4da70rlr6zs5fzt8c4sfxrjfvw8qyuuz3naw9dajw02uhvvsv8rryfkyeaerqpaqxj3n', 'lntb1m1pjdcqvzpp5u3lvv9yjkec99r6j7s725gyjgxv3gw6k06kwmwtcl4uv594gjuwqdqqcqzzsxq9z0rgqsp5eewsmglcz96a8tr69jkrav7pyjx7chh539z9uztg3s5ymfqkul7q9q8pqqqssq0zrhql0e4fdwhrrw94nc464gqp3yqet9wskc9dc6zvzy7mpyrmgn6n3h3v76978j8yfqyd7spdw593p3458u40mtw8sngc32pwlcxucprhkt06', 'lntb1m1pjdcqvzpp5npzd7snmud2394kh0r96z6dp4c6t8ry2hxtpmw3e2l87k54vg4xqdqqcqzzsxq9z0rgqsp5wq2pzjl2cph5zh4v4r5q8vv5ykuc3ae0c2ap6y6d2k6yejcnqwns9q8pqqqssqmssc926gchczd39cqp7jsh4p7tw678f40rxvtzv9rs3jqmns58jhu54ggk6mwpk6jw629u020fz545ucks0zw3paq5j2k7sl3r45juqpgx290m', 'lntb1m1pjdcqvzpp5hkqaf0a7h69p82tq0fdkggza954dag2e2q9q6cf449pszamw0zqsdqqcqzzsxq9z0rgqsp555emha57l7t0js4l06hrxwwcalqgrpcw48ufuey5h54hyw2pxl0s9q8pqqqssqfgaj6pdqt48vfg2rgf24amdvn0y80mmnnm7hgms4k5ctad3y5z9zkzh5cxdhchmqzzt8eauazqsj3peqzx4tzyswjdhnmska63jt8scpkp0axg', 'lntb1m1pjdcqvzpp58zu2rjstjrxwk60sfr5qtwddk7045nw6l3vd9ky8s5cupucsy3tsdqqcqzzsxq9z0rgqsp5vz7nu2vlrdq3fvhcsdfd9zzynj2yxwhnewaqlq9exr39xcrxknps9q8pqqqssqa0zsmhc2ftqd273fgyxl40yn50346g3fnj7t0dd2hnkf64ymjny5unyrv0skgs99hw8et3zjz3p2fqezme8sz35056zq96rn2kd86kcqx070s9', 'lntb1m1pjdcqvzpp5jm7eqgh6nre5xhrkaf8jm9ed855s8uph3qche4epqxymdlxyz59sdqqcqzzsxq9z0rgqsp5cr86jyauatlkthdesjndgzcjl4tu6thwr73qs22rs397k7jgqzus9q8pqqqssq3z4xq6gpjwymkmk2drmvm4cetzwcqnezd2azz8cl5xqu65q3zs78zv2qry34uvpvgt98jz703smc5cl6wcl6h3amp3a67pvl3rtn32sp6taurw', 'lntb1m1pjdcqvzpp5ry63hyn76yzqn04y37092jza0sclddk7f52c5t7jer2lfyah9hmsdqqcqzzsxq9z0rgqsp50nyfmu2fdsexd83k9gstvw26tf47aljmjpvpqjusazvghutfa0cs9q8pqqqssq849t2xfn9cfasgthts9989dmtt8296v60tyhdkpyu5ll3gqjkn7ymj0m7ger8y6knjnvd6cjmpj2p6ethgh2du7xk6qp6ucv3amcdrgpy3yjju', 'lntb1m1pjdcqvzpp5ae87f9h6uvlrtqcvtetxnsu0yqgf5tcrhf5fmagp03v90a0up94sdqqcqzzsxq9z0rgqsp5wer27p5yg6986wp44yc58kkc57vdpspfh4sggg4gnm238x4qfpuq9q8pqqqssqnzj5z9cf88w3rk6uc7d0xewxdhyuy9qgjhulp95ud34f9uy4nsesumumnw6sm420htef679u3gnxpw9vfkemfk33xplpp4fa7l66awcqzrlxsc', 'lntb1m1pjdcqvzpp552xqpmyqvszze7r78fvefmsyjv64gc5dvvpze7944rgtt8gnt0vqdqqcqzzsxq9z0rgqsp5afjme0e7dyfzktp760hdz39pt4a82mwzrzp2zeyxgp5kyq38hzzq9q8pqqqssqhaju8lzyx220hr2p3024mv2eje30zlsdrzv207k0vcvyxwdspw9996crygvy2n3g024w9gfge00ap8wr4w3u6nm7krp5k4wthamp0aqpl6wfng', 'lntb1m1pjdcqvzpp5pvc4dhcjk66wv050vpuc2mdh432xn705mn7p6847chgrcvawwmtqdqqcqzzsxq9z0rgqsp5uqa5ghyhqghh7vf4y7w4nqwxl8mdv2fnkldk64h60jvkrxvwj7rs9q8pqqqssqx8eyzhsdkwqnk3lf2rlygan2e9ryrah0vcs0ssvd62ss5xag4ryxtxnjd0mtmdxfj8sn52tqlwy09kjvvfwxdh6dwhcal8uevvkruasqx4kqcg', 'lntb1m1pjdcqvzpp5stslytvm8vktunwv42j8chzhk9nxk6022ng5vt7prxmvagcdlslqdqqcqzzsxq9z0rgqsp56xxscr4wn968xhsc6ws0l4v6ap87lguj7gcsm3n3qdue7drf52ds9q8pqqqssqjezumupffw5u42820gqzuuhckgnkp7tkg8rx46v0hjgkmnc4j4cn2d34k6wyddnzuz0er3w00jxhyhg9w63f4k4wf9vwm6cmhsyk4wgq90dx9f', 'lntb1m1pjdcqvzpp5dk6w7tut7wwvgen3zwa6d6kan3rx8nalany64t7x2s76wtfuhqvqdqqcqzzsxq9z0rgqsp5p3z5unsgye9jysdgysnq462m7nlc2y007a6ycdxk4z6ewnacmuus9q8pqqqssq47ytm5gdz9fr9sm0jxshgw5dk04tpfd36d6sd44l2x8y99sj0d25d0kpre3zkulf9gqtdcfmj7ker4htsppgp7f9nvd2455kvr9kvmsq9ahf57', 'lntb1m1pjdcqvzpp58ajdh9qnz4fu93xpzm2qyqy7zms98xfmnanurgflzty2nwtzeqnsdqqcqzzsxq9z0rgqsp52rvc6d55xl05p2lnln39gcnptpn2up93tt0grjshmh938hekg2hq9q8pqqqssqplacs7phanhrw63pnetekelcr7r9ypdzvjpuk6rsnrpktwm9a30jnflr2555gn0ru668xxxuzwcc76pjymrvsq37w0fxjlrh0tk302qp4s2nak', 'lntb1m1pjdcqvzpp5vj0q3p84vw3v0y3e3u5jqq5yp8skm0e8pqhyh654u49qz659smnqdqqcqzzsxq9z0rgqsp56fhvjqt0q6r0yy65g8py9x4k244jhhrluq8lnq4c3d9khlajehhq9q8pqqqssq8nn0gmycv5l9z6xq9lhq2jq0hk0xykz9d3qhc67dt7maseaqx5mx9y8q3us6c4pvr0uqzvqr7jpycwjn7puweujlq0gwm6gqqszkvwsqgkag7e']
payment_amount = 100000
peer_address = '03f67cc0cad43f0485eff665769d6b0bd14fede93cf8fca7b8a9467d071e4c1366'
num_channels = 7

success =0
fail = 0

for i in range(0, len(invoices)):
  print("Successes: {}\nFails: {}".format(success, fail))
  print("Opening Channels:".format(invoices[i]))
  print("")
  output = ''
  error = ''
  for i in range(0, num_channels):

    # Loop to avoid limiation on pending channels
    print("Waiting for pending channels to open to continue opening...")
    while(1):
      result = subprocess.run(['lncli', '-n', 'testnet', 'pendingchannels'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      output = result.stdout.decode('utf-8')
      num_pending_channels = len(json.loads(output)['pending_open_channels'])
      if num_pending_channels < 10:
        break
    print("Done waiting for pendning channels < 10")
    print("")

    print("Generating channel {} of amount: {}".format(i+1, 50000))
    result = subprocess.Popen(['lncli','-n', 'testnet', 'openchannel', peer_address, str(50000)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    print(output.decode('ascii'))
    print(error.decode('ascii'))
    if len(error.decode('ascii')) > 0:
      break
  if len(error.decode('ascii')) > 0:
    break

  print("")
  print("Waiting for channels to open..")
  print("")
  while(1):
    result = subprocess.run(['lncli', '-n', 'testnet', 'pendingchannels'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    num_pending_channels = len(json.loads(output)['pending_open_channels'])
    if num_pending_channels == 0:
      print("Channels have opened.")
      break

  print("")
  print("Paying Invoice:")
  start_time = time.time()
  result = subprocess.Popen(['lncli','-n', 'testnet', 'payinvoice', invoices[i]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
  result.stdin.write(b'yes\n')
  output, error = result.communicate()
  result.stdin.close()
  elapsed_time = time.time() - start_time
  print(output.decode('ascii'))
  print(error.decode('ascii'))

  if "SUCCEEDED" not in output.decode('ascii'):
    print("Payment Error:")
    fail += 1
    i -= 1
    num_channels -= 1
  else:
    file = open('data/channels_vs_time_fulfill.txt', 'a')
    file.write('{};{}\n'.format(num_channels, elapsed_time))
    file.close()
    print("Payment Success:")
    success += 1

  print("")
  print("Closing all open channels...")
  result = subprocess.run(['lncli','-n', 'testnet', 'closeallchannels'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  while(1):
    result = subprocess.run(['lncli', '-n', 'testnet', 'pendingchannels'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    num_pending_channels = len(json.loads(output)['waiting_close_channels'])
    if num_pending_channels == 0:
      print("Channels have closed.")
      break

  num_channels += 1

print("Success Ratio: {}".format(success/(success+fail)))
