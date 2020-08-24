class Collection < ApplicationRecord
  has_many :skins, before_add: [:check_category, :check_weight_class],
                   after_add:  :set_unlocked

  validates_presence_of :name, :category

  def update_unlocked
    update(unlocked: skins.pluck(:unlocked).all?(true))
  end

  private

  def check_category(skin)
    if category.nil?
      self.category = skin.category
    else
      raise 'Category mismatch' if category != skin.category
    end
  end

  def check_weight_class(skin)
    if category == 'Armor' && weight_class.nil?
      self.weight_class = skin.weight_class
    else
      raise 'Weight class mismatch' if weight_class != skin.weight_class
    end
  end

  def set_unlocked(skin)
    update_unlocked
  end
end
