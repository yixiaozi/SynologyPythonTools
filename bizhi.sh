save="/volume2/homes/yixiaozi/Wallpaper/bing.jpg"
#�����Ҫ�ռ�����ÿ����ͼ��ȥ��ע��
#����·��path���������Լ����ļ��У���FileStation�����Ҽ��ļ������Կ��Կ���·��
path="/volume2/photo/Bing"
name="$(date +'%Y%m%d')_bing.jpg"
save=$path$name
wget "https://bing.com$(curl -s "https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"|sed 's/.\+"url"[:" ]\+//g'|sed 's/".\+//g')" -qO $save
story=$(curl -s https://www4.bing.com/cnhp/coverstory)
sed -i s/login_background_customize=.*//g /etc/synoinfo.conf
echo login_background_customize=\"yes\">>/etc/synoinfo.conf
ln -sf $save /usr/syno/etc/login_background_hd.jpg
ln -sf $save /usr/syno/etc/login_background.jpg
if (echo $story|grep attribute) then
sed -i s/login_welcome_title=.*//g /etc/synoinfo.conf
echo "login_welcome_title=\"$(echo $story|sed 's/.\+"title"[: "]\+//g'|sed 's/",".\+//g')\"">>/etc/synoinfo.conf
sed -i s/login_welcome_msg=.*//g /etc/synoinfo.conf
echo "login_welcome_msg=\"$(echo $story|sed 's/.\+"attribute"[: "]\+//g'|sed 's/",".\+//g')\"">>/etc/synoinfo.conf
fi
#�����û����汳��
ln -sf $save /usr/syno/etc/preference/admin/wallpaper