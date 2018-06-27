package com.isoftstone.cloud.channel.process.common.enums;
/**
 * 使用规范:
 * 1.枚举类名建议带上Enum 后缀
 * 2.枚举成员名称要大写
 * 3.枚举其实就是特殊的常量类
 * 4.所有枚举类型字段必须要有注释 说明每个数据项的作用
 * 5.构造函数强制私有
 */
public enum TYPEEnum {

    ANIMAL("animal"),
    PEOPLE("people"),
    STUDENT("student");

    //自定义属性
    private String typeName;

    private TYPEEnum(String typeName){
        this.typeName =typeName;
    }
    public String getTypeName(){
        return this.typeName;
    }
    public static TYPEEnum getTypeByName(String typeName){
        for(TYPEEnum type: TYPEEnum.values()){
            System.out.println(type.getTypeName());
            System.out.println(type.name()); //枚举成员名称
            System.out.println(type.ordinal()); //枚举类成员排序
            System.out.println("==============");

            if(type.getTypeName().equals(typeName)) return type;
        }
        return null;
    }
}

class TYPEEumTest{
    public static void main(String args[] ){
        TYPEEnum type=TYPEEnum.getTypeByName("student");
        System.out.println(type);
    }
}